# Autonomous AI Orchestrator

**Fully autonomous code generation → test → deploy pipeline powered by AI agents.**

Once onboarded, a user provides an Epic or a complete Project Requirements document through the web interface. The agentic system then designs, develops, tests, and deploys an enterprise-grade application — with every Epic living in its own isolated GitHub repository.

> **Status:** Active development (POC). Backend foundation (Flask application factory, health endpoints, CI, Docker) is on `main`. Frontend and full agent orchestration are in progress. See [Issues](https://github.com/TonyRolfe/autonomous-ai-orchestrator/issues) for Epics and User Stories.

---

## Vision

| Stage | What happens |
|-------|--------------|
| 1. Conversational entry | User describes an Epic or pastes requirements in chat |
| 2. Repo isolation | System creates a private GitHub repo for that Epic |
| 3. Agent orchestration | CrewAI / LangChain agents generate architecture, code, tests |
| 4. Quality gates | 100% coverage, lint, type-check, security scans must pass |
| 5. Deploy | Dockerized deployment when CI is fully green |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Flask 3 + application factory pattern |
| Agents | LangChain / CrewAI |
| Frontend | React 18 + TypeScript + Vite + Tailwind CSS *(in progress)* |
| LLM | Azure OpenAI **or** IBM watsonx (user-selectable) |
| Database | PostgreSQL + SQLAlchemy + Alembic *(planned – US-06)* |
| Testing | pytest (target 100% line + branch) + Jest/RTL |
| CI | GitHub Actions: ruff, black, mypy, pytest-cov, bandit, safety |
| Deployment | Docker + docker-compose |

---

## Project Rules (Non-Negotiable)

- **100% test coverage** (line + branch) before merge
- Auto-merge **only** when CI is fully green
- Clean code: SOLID · KISS · DRY enforced on every change
- Secrets never committed; all credentials via environment variables
- One private GitHub repository per Epic

---

## Quick Start (Development)

### Prerequisites
- Docker & Docker Compose
- Python 3.12+ (for local non-Docker runs)
- A GitHub PAT with `repo` scope (for Epic repo creation)
- Azure OpenAI **or** IBM watsonx credentials

### 1. Clone & configure

```bash
git clone https://github.com/TonyRolfe/autonomous-ai-orchestrator.git
cd autonomous-ai-orchestrator
cp .env.example .env
# Edit .env with your secrets
```

### 2. Start the stack

```bash
docker compose up --build
```

| Service | URL |
|---------|-----|
| Backend API | http://localhost:5000 |
| Health check | http://localhost:5000/health |
| Frontend (Vite) | http://localhost:3000 |
| PostgreSQL | localhost:5432 |

### 3. Run tests locally

```bash
pip install -r requirements.txt
PYTHONPATH=. pytest tests/ -v --cov=src/backend --cov-report=term-missing
```

---

## Repository Layout

```
.
├── .github/workflows/ci.yml   # CI pipeline
├── src/backend/app/           # Flask application factory, config, routes, services
├── tests/                     # pytest suite
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Roadmap (POC)

### Epic 1 – Platform Bootstrap & Conversational Entry Point
- [x] US-03 Backend skeleton (Flask + CI) — **landed on main**
- [ ] US-01 Conversational web UI
- [ ] US-02 Auto-create GitHub repository per Epic

### Epic 2 – Authentication & Secrets Management
- [ ] US-04 Secure login / sign-up flow
- [ ] US-05 Connect & manage personal GitHub credentials
- [ ] US-06 Production-grade PostgreSQL + SQLAlchemy + Alembic
- [ ] US-07 Use authenticated user’s GitHub credentials for repo creation
- [ ] US-08 Encrypted storage of GitHub PATs & secret scanning
- [ ] US-09 Authentication with TOTP MFA and recovery codes

Daily progress is tracked in issues labeled `progress`.

---

## Required Secrets (see `.env.example`)

| Variable | Purpose |
|----------|---------|
| `GITHUB_TOKEN` | PAT with `repo` scope |
| `SECRET_KEY` | Flask session signing |
| Azure OpenAI **or** watsonx credentials | LLM provider (choose one) |
| `POSTGRES_*` / `DATABASE_URL` | Database (when US-06 lands) |

---

## Contributing / Portfolio Notes

This repository is part of a public portfolio. PRs and issues that advance the roadmap above are welcome. All contributions must keep CI green and respect the project rules.

---

*Built with Flask, CrewAI, and a commitment to enterprise-grade quality from day one.*
