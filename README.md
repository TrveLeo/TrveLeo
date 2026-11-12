<p align="center">
  <img src="img/header.svg" alt="Floresta escura com uma onda senoidal no céu" width="100%">
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=UnifrakturMaguntia&size=52&duration=3000&pause=100000&color=E6E6E6&center=true&vCenter=true&repeat=false&width=700&height=80&lines=Leandro+Baldan" alt="Leandro Baldan">
  <br>
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=16&duration=2800&pause=1200&color=8A8A8A&center=true&vCenter=true&width=600&height=30&lines=Engenheiro+eletricista+em+forma%C3%A7%C3%A3o;Desenvolvedor+back+end+em+Python;Metal+no+fone%2C+xadrez+no+intervalo" alt="Engenheiro eletricista em formação, desenvolvedor back end em Python">
</p>

<p align="center">
  <a href="https://trveleo.github.io/TrveLeo/"><img src="https://img.shields.io/badge/portf%C3%B3lio-0d0d0d?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfólio"></a>
  <a href="https://www.linkedin.com/in/leandro-baldan/"><img src="https://img.shields.io/badge/linkedin-0d0d0d?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:leandrobaldan.contato@gmail.com"><img src="https://img.shields.io/badge/e--mail-b3261e?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail"></a>
</p>

### ♟ 1. e4 · quem sou

Oi! Sou o Leandro, de Vitória (ES). Estudo Engenharia Elétrica no IFES (termino em meados de 2027) e cheguei ao software pelo caminho da energia: comecei como estagiário em O&M de usinas solares e hoje escrevo o back end que monitora essas usinas.

Na **Mola Mola** cuido da plataforma que acompanha **45 usinas fotovoltaicas de 7 organizações**, puxando dados de 6 portais diferentes, SCADA locais e APIs de inversores. Boa parte do trabalho é fazer dado ruim, API instável e fuso horário errado virarem uma série temporal confiável.

Fora do código, quase sempre tem metal tocando e, nas pausas, xadrez. Gosto de software livre e de conhecimento compartilhado, por isso meus projetos pessoais ficam públicos aqui.

<p align="center">
  <a href="https://open.spotify.com/user/a3g1nlz37cyjftlznm0rxwvg5"><img src="https://spotify-github-profile.kittinanx.com/api/view?uid=a3g1nlz37cyjftlznm0rxwvg5&cover_image=true&theme=default&show_offline=false&background_color=0d0d0d&bar_color=b3261e&bar_color_cover=false&interchange=false&profanity=false&hide_remaster=false" alt="O que estou ouvindo no Spotify"></a>
</p>

<p align="center"><img src="img/divider.svg" alt="" width="60%"></p>

### ♞ 2. Cf3 · o que faço no dia a dia

- ⚡ **APIs e serviços** em Django REST e FastAPI, com Celery para ingestão, reconciliação e backfill de séries temporais em PostgreSQL/TimescaleDB.
- 🔌 **Integrações** com OAuth, retry e fallback para rate limit, indisponibilidade e dado faltando. Parto do princípio de que a API do outro lado vai cair.
- 🐳 **Docker e CI/CD** com GitHub Actions: lint, testes, deploy em staging e produção, rollback e health checks.
- 🧠 **IA em produção**: classificação de alertas de inversores com LightGBM (F1 de 0,94 na detecção de anomalia), separando treino e teste por usina para não vazar dado.

<p align="center"><img src="img/divider.svg" alt="" width="60%"></p>

### ♝ 3. Bc4 · projetos

Projetos pessoais com dados fictícios. Os números saem dos testes de cada repositório, então dá para reproduzir.

| Projeto | O que faz | Resultado | Stack |
|---|---|---|---|
| [ChatDesk](https://github.com/TrveLeo/chatdesk) | Atendimento que responde só com o que está nos documentos da empresa, cita a fonte e recusa o que não sabe | 206 testes, 100% de cobertura | FastAPI · pgvector · RAG |
| [ClauseGuard](https://github.com/TrveLeo/clauseguard) | Agente que audita contrato contra a política da empresa e para pedindo revisão humana quando o risco é alto | 93,3% de recall, zero falso positivo no benchmark | LangGraph · Qdrant · FastAPI |
| [LeadDesk](https://github.com/TrveLeo/leaddesk) | CRM de pipeline comercial com prospecção acoplada | 199 testes, 100% de cobertura | FastAPI · SQLAlchemy 2.0 · PostgreSQL |
| [ConciliaFlow](https://github.com/TrveLeo/conciliaflow) | Conciliação automática de planilhas de vendas e créditos, com fila de revisão | 77,2% conciliado sem intervenção, 61 testes | FastAPI · Pandas · PostgreSQL |
| [YOLOv8 + Optuna](https://github.com/TrveLeo/Otimizacao_de_arquitetura_e_hiperparametros_yolov8) | Detecção de armas de fogo em câmeras, buscando arquitetura e hiperparâmetros (pesquisa no IFES, com artigo) | Modelo menor supera o maior em precision e mAP@50 | PyTorch · YOLOv8 · Optuna |
| [Santander](https://github.com/TrveLeo/santander-customer-transaction-prediction) | Classificação binária de transações bancárias (Kaggle) | 0,9181 de AUC-ROC out-of-fold contra 0,8997 do baseline | LightGBM · scikit-learn |

<p align="center"><img src="img/divider.svg" alt="" width="60%"></p>

### ♜ 4. O-O · stack

<p>
  <img src="https://img.shields.io/badge/Python-0d0d0d?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-0d0d0d?style=flat-square&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/FastAPI-0d0d0d?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Celery-0d0d0d?style=flat-square&logo=celery&logoColor=white" alt="Celery">
  <img src="https://img.shields.io/badge/PostgreSQL-0d0d0d?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/TimescaleDB-0d0d0d?style=flat-square&logo=timescale&logoColor=white" alt="TimescaleDB">
  <img src="https://img.shields.io/badge/Docker-0d0d0d?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub_Actions-0d0d0d?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Linux-0d0d0d?style=flat-square&logo=linux&logoColor=white" alt="Linux">
  <img src="https://img.shields.io/badge/Pytest-0d0d0d?style=flat-square&logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/LangGraph-0d0d0d?style=flat-square&logo=langchain&logoColor=white" alt="LangGraph">  <img src="https://img.shields.io/badge/scikit--learn-0d0d0d?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/PyTorch-0d0d0d?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch">
</p>

<p align="center"><img src="img/divider.svg" alt="" width="60%"></p>

### ♛ 5. d3 · atividade

<p align="center">
  <img src="img/stats/heatmap.svg" alt="Calendário de contribuições do último ano" width="100%">
</p>
<p align="center">
  <img src="img/stats/weekdays.svg" alt="Contribuições por dia da semana" width="49%">
  <img src="img/stats/languages.svg" alt="Linguagens mais usadas" width="49%">
</p>

<p align="center"><sub>atualizado todo dia por um GitHub Action deste repositório. Inclui contribuições em repositórios privados.</sub></p>

<p align="center"><img src="img/divider.svg" alt="" width="60%"></p>

### ♚ 6. … · vamos conversar

Estou aberto a oportunidades como desenvolvedor back end. Se quiser trocar ideia sobre Python, dados de energia, agentes de IA ou uma partida de xadrez, me chama em **leandrobaldan.contato@gmail.com** ou no [LinkedIn](https://www.linkedin.com/in/leandro-baldan/).

<p align="center"><sub>★ conhecimento bom é conhecimento compartilhado</sub></p>
