.PHONY: install test lint format typecheck pre-commit docker-up docker-down health

# Install dependencies and pre-commit hooks
install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install pre-commit
	pre-commit install

# Run tests with coverage (90% gate)
test:
	PYTHONPATH=. pytest tests/ -v --cov=src/backend --cov-report=term-missing --cov-fail-under=90

# Lint
lint:
	ruff check src tests

# Format
format:
	black src tests
	isort --profile black --line-length 100 src tests

# Type check
typecheck:
	mypy src/backend --ignore-missing-imports

# Run all pre-commit hooks
pre-commit:
	pre-commit run --all-files

# Start the full stack
docker-up:
	docker compose up --build -d

# Stop the stack
docker-down:
	docker compose down

# Health check
health:
	curl -s http://localhost:5000/health | python -m json.tool
