# Autonomous AI Orchestrator

Fully autonomous code generation → test → deploy pipeline powered by AI agents. Once fully onboarded, a user provides the web interface with an Epic or a complete Project Requirements document and the agentic system develops, tests, and deploys an enterprise-grade application.

---

## Current Status (July 2026)

- **Stage**: Early skeleton / bootstrap
- Backend source files (`main.py`, `config.py`, routes, services) are placeholders ready for implementation of US-03
- Docker Compose + Dockerfiles present
- Strong issue backlog for Epic 1 (bootstrap) and Epic 2 (auth + secrets)
- Project rules enforced: 100% test coverage, clean code, CI-green-only auto-merge

See open issues for detailed user stories (US-03 backend skeleton is the immediate next priority).

---

## Tech Stack

- **Backend**: Flask + LangChain / CrewAI
- **Frontend**: React 18 + TypeScript + Vite + Tailwind CSS
- **LLM**: Azure OpenAI or IBM watsonx (user-selectable)
- **Database**: PostgreSQL + SQLAlchemy (when required)
- **Testing**: pytest (100% coverage target) + Jest / RTL (frontend)
- **CI**: GitHub Actions (mypy, ruff, black, isort, bandit, safety)
- **Deployment**: Docker + docker-compose

---

## Quick Start (Development)

```bash
# Start both services
docker compose up --build

# Backend runs on http://localhost:5000
# Frontend (Vite) runs on http://localhost:3000 → proxied to Flask in dev
```

---

## Required Secrets (see `.env.example`)

- `GITHUB_TOKEN` – PAT with `repo` scope
- Azure OpenAI **or** IBM watsonx credentials (one provider only)

---

## Project Rules (Non-Negotiable)

- 100% test coverage (line + branch)
- Auto-merge only when CI is 100% green
- Clean code / SOLID / KISS / DRY enforced on every line

---

## Roadmap (High Level)

1. **US-03** – Complete backend skeleton (Flask app factory, config, health routes, basic services, tests)
2. **Epic 2** – Authentication & secrets management (login, GitHub PAT storage, PostgreSQL, MFA, etc.)
3. Conversational UI + auto-repo creation (Epic 1 remaining stories)
4. Full agent orchestration loops (code gen → test → deploy)
5. Production hardening + portfolio demos

---

## Contributing / Daily Progress

Daily progress is tracked in issues labeled `progress`. Feel free to open issues or PRs aligned with the user stories.

---

Built by [Tony Rolfe](https://github.com/TonyRolfe) · Portfolio project
