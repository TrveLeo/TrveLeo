"""Generate themed GitHub stats SVGs for the profile README.

Reads the public GitHub GraphQL API and writes three SVGs into img/stats/:
  - heatmap.svg:   last-year contribution calendar plus streak/total numbers
  - weekdays.svg:  contribution distribution per weekday
  - languages.svg: language share across public, non-fork owned repos

Only the standard library is used, so the workflow needs no install step.
Requires GITHUB_TOKEN in the environment. Usage: python scripts/gen_stats.py [user]
"""
import datetime as dt
import json
import os
import sys
import urllib.request
from html import escape
from pathlib import Path

USER = sys.argv[1] if len(sys.argv) > 1 else "TrveLeo"
OUT_DIR = Path(__file__).resolve().parent.parent / "img" / "stats"

BG = "#0d0d0d"
TEXT = "#c9c9c9"
MUTED = "#6e6e6e"
RED = "#b3261e"
# empty cell first, then increasing intensity (dark grey to blood red)
HEAT = ["#1a1a1a", "#3d1210", "#651a16", "#8c201a", "#b3261e"]
FONT = "font-family=\"'JetBrains Mono',Consolas,'DejaVu Sans Mono',monospace\""
WEEKDAYS = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
MONTHS = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
IGNORED_LANGS = {"Dockerfile", "Makefile", "Shell", "Batchfile", "PowerShell"}

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount weekday } }
      }
    }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      nodes { languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name } } } }
    }
  }
}
"""


def fetch(token):
    """Run the GraphQL query and return the user node."""
    body = json.dumps({"query": QUERY, "variables": {"login": USER}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "profile-stats-generator"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if payload.get("errors"):
        raise RuntimeError(f"GraphQL errors: {payload['errors']}")
    return payload["data"]["user"]


def streaks(days):
    """Return (current, longest) streaks of consecutive days with contributions."""
    longest = run = 0
    for day in days:
        run = run + 1 if day["contributionCount"] > 0 else 0
        longest = max(longest, run)
    current = 0
    today = dt.date.today().isoformat()
    for day in reversed(days):
        if day["contributionCount"] > 0:
            current += 1
        elif day["date"] == today:
            continue  # today without commits yet does not break the streak
        else:
            break
    return current, longest


def level(count, peak):
    """Map a day count to a HEAT index using quartiles of the peak."""
    if count == 0:
        return 0
    return min(4, 1 + int(3 * count / max(peak, 1) + 0.5))


def svg(width, height, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" {FONT}>'
            f'<rect width="{width}" height="{height}" rx="8" fill="{BG}"/>{inner}</svg>')


def heatmap(calendar):
    weeks = calendar["weeks"]
    days = [d for w in weeks for d in w["contributionDays"]]
    peak = max((d["contributionCount"] for d in days), default=0)
    current, longest = streaks(days)
    active = sum(1 for d in days if d["contributionCount"] > 0)
    cell, gap, left, top = 13, 3, 44, 92
    width = left + len(weeks) * (cell + gap) + 20
    height = top + 7 * (cell + gap) + 40
    parts = []
    stats = [
        (f"{calendar['totalContributions']:,}".replace(",", "."), "contribuições no último ano"),
        (str(active), "dias com contribuição"),
        (f"{current} d", "sequência atual"),
        (f"{longest} d", "maior sequência"),
    ]
    col = (width - 40) / len(stats)
    for i, (value, label) in enumerate(stats):
        x = 20 + col * i
        parts.append(f'<text x="{x:.0f}" y="44" fill="{RED if i == 0 else "#e6e6e6"}" font-size="24" '
                     f'font-weight="700">{escape(value)}</text>')
        parts.append(f'<text x="{x:.0f}" y="64" fill="{MUTED}" font-size="11">{escape(label)}</text>')
    last_month = None
    for wi, week in enumerate(weeks):
        x = left + wi * (cell + gap)
        first = dt.date.fromisoformat(week["contributionDays"][0]["date"])
        if first.month != last_month and first.day <= 7:
            parts.append(f'<text x="{x}" y="{top - 8}" fill="{MUTED}" font-size="10">{MONTHS[first.month - 1]}</text>')
            last_month = first.month
        for day in week["contributionDays"]:
            y = top + day["weekday"] * (cell + gap)
            fill = HEAT[level(day["contributionCount"], peak)]
            parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{fill}">'
                         f'<title>{day["date"]}: {day["contributionCount"]}</title></rect>')
    for wd in (1, 3, 5):
        parts.append(f'<text x="12" y="{top + wd * (cell + gap) + 10}" fill="{MUTED}" font-size="10">'
                     f'{WEEKDAYS[wd]}</text>')
    legend_y = height - 22
    lx = width - 20 - 5 * (cell + gap) - 70
    parts.append(f'<text x="{lx - 8}" y="{legend_y + 10}" fill="{MUTED}" font-size="10" text-anchor="end">menos</text>')
    for i, color in enumerate(HEAT):
        parts.append(f'<rect x="{lx + i * (cell + gap)}" y="{legend_y}" width="{cell}" height="{cell}" rx="2" '
                     f'fill="{color}"/>')
    parts.append(f'<text x="{lx + 5 * (cell + gap) + 4}" y="{legend_y + 10}" fill="{MUTED}" font-size="10">mais</text>')
    return svg(width, height, "".join(parts)), days


def weekdays(days):
    totals = [0] * 7
    for day in days:
        totals[day["weekday"]] += day["contributionCount"]
    peak = max(totals) or 1
    width, height, base, bar_w = 450, 230, 180, 38
    parts = [f'<text x="20" y="32" fill="#e6e6e6" font-size="14" font-weight="700">Frequência por dia da semana</text>']
    for i, total in enumerate(totals):
        h = 120 * total / peak
        x = 30 + i * 58
        color = RED if total == peak else "#5a1a16"
        parts.append(f'<rect x="{x}" y="{base - h:.1f}" width="{bar_w}" height="{h:.1f}" rx="3" fill="{color}"/>')
        parts.append(f'<text x="{x + bar_w / 2}" y="{base - h - 6:.1f}" fill="{TEXT}" font-size="11" '
                     f'text-anchor="middle">{total}</text>')
        parts.append(f'<text x="{x + bar_w / 2}" y="{base + 18}" fill="{MUTED}" font-size="11" '
                     f'text-anchor="middle">{WEEKDAYS[i]}</text>')
    return svg(width, height, "".join(parts))


def languages(repos, top_n=6):
    sizes = {}
    for repo in repos:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            if name not in IGNORED_LANGS:
                sizes[name] = sizes.get(name, 0) + edge["size"]
    total = sum(sizes.values()) or 1
    ranked = sorted(sizes.items(), key=lambda kv: -kv[1])[:top_n]
    shades = [RED, "#8c201a", "#651a16", "#8a8a8a", "#5e5e5e", "#3d3d3d"]
    width, height = 450, 230
    parts = [f'<text x="20" y="32" fill="#e6e6e6" font-size="14" font-weight="700">Linguagens mais usadas</text>']
    x = 20.0
    bar_w = width - 40
    for i, (_, size) in enumerate(ranked):
        w = bar_w * size / total
        parts.append(f'<rect x="{x:.1f}" y="50" width="{max(w, 1):.1f}" height="10" fill="{shades[i]}"/>')
        x += w
    for i, (name, size) in enumerate(ranked):
        cx = 20 + (i % 2) * 215
        cy = 92 + (i // 2) * 34
        parts.append(f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{shades[i]}"/>')
        parts.append(f'<text x="{cx + 18}" y="{cy}" fill="{TEXT}" font-size="12">{escape(name)} '
                     f'<tspan fill="{MUTED}">{100 * size / total:.1f}%</tspan></text>')
    parts.append(f'<text x="20" y="{height - 16}" fill="{MUTED}" font-size="10">'
                 f'repositórios públicos, por bytes de código</text>')
    return svg(width, height, "".join(parts))


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is not set")
    user = fetch(token)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    heat_svg, days = heatmap(user["contributionsCollection"]["contributionCalendar"])
    (OUT_DIR / "heatmap.svg").write_text(heat_svg, encoding="utf-8")
    (OUT_DIR / "weekdays.svg").write_text(weekdays(days), encoding="utf-8")
    (OUT_DIR / "languages.svg").write_text(languages(user["repositories"]["nodes"]), encoding="utf-8")
    print(f"wrote stats SVGs to {OUT_DIR}")


if __name__ == "__main__":
    main()
