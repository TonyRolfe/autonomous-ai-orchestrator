# Autonomous AI Orchestrator

Fully autonomous code generation → test → deploy pipeline powered by AI agents. The user once fully onboarded will be able to provide the web interface with an Epic or a complete Project Requirements document and the Agentic system will develop, test and deploy a Enterprise Grade application.

---
## Tech Stack
- Backend: Flask + LangChain/CrewAI
- Frontend: React 18 + TypeScript + Vite + Tailwind CSS
- LLM: Azure OpenAI or IBM watsonx (user-selectable)
- Database: PostgreSQL + SQLAlchemy (only when required)
- Testing: pytest (100% coverage) + Jest/RTL (frontend)
- CI: GitHub Actions (mypy, ruff, black, isort, bandit, safety)
- Deployment: Docker + docker-compose

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
- `GITHUB_TOKEN` - PAT with `repo` scope.
- Azure OpenAI (for CoPilot integration) or IBM watsonx credentials (one provider only)

---
## Project Rules (Non-Negotiable)
- 100% test coverage (line + branch)
- Auto-merge only when CI is 100% green
- Clean code / SOLID / KISS / DRY enforced on every line