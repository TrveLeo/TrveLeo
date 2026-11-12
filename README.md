# Leandro Baldan

**Desenvolvedor Back End | Python, APIs REST e IA aplicada**

Vitória, ES | Engenharia Elétrica no IFES (conclusão prevista para 06/2027)

Desenvolvo back end em Python para sistemas que precisam ficar no ar e ter dados confiáveis. Hoje trabalho na **Mola Mola**, na plataforma de monitoramento de usinas fotovoltaicas que integra **45 usinas de 7 organizações**, a partir de 6 portais e APIs diferentes. Fora do trabalho, construo APIs com FastAPI, agentes de IA e sistemas com RAG, sempre com testes automatizados.

[Portfólio](https://leandrobaldan.vercel.app) | [LinkedIn](https://www.linkedin.com/in/leandro-baldan/) | leandrobaldan.contato@gmail.com

---

## No dia a dia

- **APIs e serviços:** Django REST, Celery e PostgreSQL/TimescaleDB para ingestão, reconciliação e backfill de séries temporais.
- **Integrações:** OAuth, retry e fallback para rate limit, indisponibilidade e dados ausentes. Desenho para falhas parciais e eventual consistency.
- **Containers e CI/CD:** deploys com Docker e GitHub Actions (lint, type checking, testes, staging, produção, rollback, health checks).
- **IA em produção:** classificação de alertas de inversores com LightGBM (F1 de 0,94 na detecção de anomalia), validação agrupada por usina para evitar vazamento de dados.
- **Agentes de código:** uso diário de Claude Code, servidores MCP e skills próprias, com cada tarefa em git worktree e stack Docker Compose isolada.

---

## Projetos

Todos com dados fictícios e resultados reproduzíveis por teste. Os repositórios são públicos.

| Projeto | O que faz | Resultado | Stack |
|---|---|---|---|
| [ChatDesk](https://github.com/TrveLeo/chatdesk) | Atendimento que responde só com o que está nos documentos da empresa, cita a fonte e recusa o que não sabe | 206 testes, 100% de cobertura | Python · FastAPI · pgvector · RAG · Docker Compose |
| [ClauseGuard](https://github.com/TrveLeo/clauseguard) | Agente que audita contrato contra a política da empresa, com portão humano para risco alto | 93,3% de recall, zero falso positivo no benchmark | Python · LangGraph · Claude · Qdrant · FastAPI |
| [LeadDesk](https://github.com/TrveLeo/leaddesk) | CRM de pipeline comercial com prospecção acoplada | 199 testes, 100% de cobertura | Python · FastAPI · SQLAlchemy 2.0 · PostgreSQL |
| [ConciliaFlow](https://github.com/TrveLeo/conciliaflow) | Conciliação automática de planilhas de vendas e créditos, com fila de revisão | 77,2% conciliado sem intervenção manual, 61 testes | Python · FastAPI · Pandas · PostgreSQL · Docker |
| [Detecção de armas com YOLOv8](https://github.com/TrveLeo/Otimizacao_de_arquitetura_e_hiperparametros_yolov8) | Otimização de arquitetura e hiperparâmetros com Optuna, com artigo incluído | Modelo menor supera o maior em precision e mAP@50 | Python · PyTorch · YOLOv8 · Optuna |
| [Santander Customer Transaction](https://github.com/TrveLeo/santander-customer-transaction-prediction) | Classificação binária de transações (Kaggle) | 0,9181 de AUC-ROC out-of-fold contra 0,8997 do baseline | Python · LightGBM · scikit-learn |

---

## Stack

- **Back end:** Python · Django · Django REST · FastAPI · Celery · SQLAlchemy
- **Dados:** PostgreSQL · TimescaleDB · pgvector · Qdrant · Pandas
- **Infra:** Docker · Docker Compose · GitHub Actions · Linux · SSH
- **IA:** LangGraph · RAG · Claude API · MCP · scikit-learn · LightGBM · PyTorch
- **Qualidade:** Pytest · Git · pull requests · CI/CD

---

## Contato

Aberto a oportunidades como desenvolvedor back end. Me escreva em leandrobaldan.contato@gmail.com ou pelo [LinkedIn](https://www.linkedin.com/in/leandro-baldan/).
