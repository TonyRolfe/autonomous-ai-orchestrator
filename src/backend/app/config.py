"""Application configuration."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env if present (local development)
load_dotenv()


class Config:
    """Base configuration."""

    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-change-me-in-production")
    FLASK_ENV: str = os.getenv("FLASK_ENV", "development")
    DEBUG: bool = os.getenv("FLASK_DEBUG", "0") == "1"

    # GitHub
    GITHUB_TOKEN: str | None = os.getenv("GITHUB_TOKEN")
    GITHUB_USERNAME: str | None = os.getenv("GITHUB_USERNAME")

    # LLM providers (user selects one)
    AZURE_OPENAI_ENDPOINT: str | None = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_KEY: str | None = os.getenv("AZURE_OPENAI_KEY")
    AZURE_OPENAI_DEPLOYMENT: str | None = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")

    WATSONX_URL: str | None = os.getenv("WATSONX_URL")
    WATSONX_API_KEY: str | None = os.getenv("WATSONX_API_KEY")
    WATSONX_PROJECT_ID: str | None = os.getenv("WATSONX_PROJECT_ID")

    # Database
    DATABASE_URL: str | None = os.getenv(
        "DATABASE_URL",
        f"postgresql://{os.getenv('POSTGRES_USER', 'orchestrator')}:"
        f"{os.getenv('POSTGRES_PASSWORD', 'secure_password_change_me')}@"
        f"localhost:5432/{os.getenv('POSTGRES_DB', 'orchestrator_db')}",
    )
    SQLALCHEMY_DATABASE_URI: str | None = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_ENGINE_OPTIONS: dict[str, object] = {
        "pool_pre_ping": True,
        "pool_size": 5,
        "max_overflow": 10,
        "pool_timeout": 30,
    }

    # Project paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent


class TestConfig(Config):
    """Configuration for tests (in-memory SQLite)."""

    TESTING = True
    SECRET_KEY = "test-secret"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_ENGINE_OPTIONS: dict[str, object] = {}
