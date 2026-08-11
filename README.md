# Autonomous AI Orchestrator

[![CI](https://github.com/TonyRolfe/autonomous-ai-orchestrator/actions/workflows/ci.yml/badge.svg)](https://github.com/TonyRolfe/autonomous-ai-orchestrator/actions/workflows/ci.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.1-black.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Fully autonomous code generation → test → deploy pipeline powered by AI agents.**

Once onboarded, a user provides an Epic or complete Project Requirements document via the web interface. The agentic system develops, tests, and deploys an enterprise-grade application end-to-end.

> Portfolio project by [Tony Rolfe](https://github.com/TonyRolfe) · Active development · Flask + LangChain/CrewAI foundation on `main`

---

## Vision

Turn high-level product intent into running software with minimal human intervention:

1. **Ingest** requirements / Epic
2. **Plan** architecture & tasks with multi-agent orchestration
3. **Generate** code, tests, and infrastructure
4. **Validate** with automated testing (target 100% coverage)
5. **Deploy** via Docker / CI-CD

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Flask 3.1 + application factory |
| Agents | LangChain / CrewAI |
| Frontend (planned) | React 18 + TypeScript + Vite + Tailwind CSS |
| LLM | Azure OpenAI **or** IBM watsonx (user-selectable) |
| Database | PostgreSQL + SQLAlchemy + Alembic (US-06) |
| Testing | pytest (backend, ≥90% coverage gate) + Jest/RTL (frontend) |
| CI | GitHub Actions (ruff, black, mypy, pytest-cov, bandit, safety) |
| Deployment | Docker + docker-compose |

---

## Current Status (August 2026)

| Area | Status |
|------|--------|
| Backend skeleton (US-03) | ✅ On `main` — app factory, Config, `/` + `/health`, services placeholder |
| CI & quality gates | ✅ Green (≥90% coverage, lint, types) |
| Docker / docker-compose | ✅ Present (backend + frontend placeholder + Postgres) |
| Auth & secrets (Epic 2) | 🔲 Open (US-04 → US-09) |
| Agent orchestration | 🔲 Planned |
| Frontend source | 🔲 Placeholder only |

See open issues for Epics and user stories.

---

## Quick Start (Development)

```bash
# Clone
git clone https://github.com/TonyRolfe/autonomous-ai-orchestrator.git
cd autonomous-ai-orchestrator

# Copy env template and fill secrets
cp .env.example .env

# Start the stack
docker compose up --build

# Backend → http://localhost:5000
# Frontend (Vite placeholder) → http://localhost:3000
# Postgres → localhost:5432
```

Health check:

```bash
curl http://localhost:5000/health
# → {"status":"ok","service":"autonomous-ai-orchestrator"}
```

---

## Project Layout

```
autonomous-ai-orchestrator/
├── src/backend/app/
│   ├── __init__.py          # Application factory
│   ├── config.py            # Env-based Config + TestConfig
│   ├── main.py              # Entry point
│   ├── routes/              # Blueprints (health, root)
│   └── services/            # Agent orchestration placeholder
├── tests/                   # pytest suite
├── .github/workflows/ci.yml
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── requirements.txt
└── pyproject.toml
```

---

## Required Secrets

See `.env.example`. Never commit real credentials.

- `GITHUB_TOKEN` – PAT with `repo` scope
- Azure OpenAI **or** IBM watsonx credentials (one provider)
- `SECRET_KEY` – change from default in production
- Postgres credentials (defaults provided for local docker-compose)

---

## Project Rules (Non-Negotiable)

- **100% test coverage** (line + branch) target
- Auto-merge only when CI is fully green
- Clean code / SOLID / KISS / DRY enforced on every change
- Secrets never in source or logs

---

## Roadmap (High Level)

1. **Foundation** (done / in progress) – Flask skeleton, CI, Docker
2. **Auth & Secrets (Epic 2)** – multi-user login, encrypted GitHub PATs, PostgreSQL + Alembic
3. **Agent Core** – CrewAI/LangChain orchestration for code gen → test → deploy
4. **Frontend** – React chat / requirements UI
5. **Production readiness** – hardening, observability, live demos

---

## Contributing

Issues and PRs welcome. Please keep CI green and respect the project rules above.

---

Built with ❤️ by [Tony Rolfe](https://github.com/TonyRolfe) · Portfolio project