"""Tests for health and root endpoints and app factory."""

import pytest

from src.backend.app import create_app
from src.backend.app.config import Config, TestConfig
from src.backend.app.services import __doc__ as services_doc


@pytest.fixture
def client():
    app = create_app(TestConfig)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_app_returns_flask_instance():
    app = create_app(TestConfig)
    assert app is not None
    assert app.config["TESTING"] is True
    assert app.config["SECRET_KEY"] == "test-secret"
    assert app.config["DEBUG"] is False


def test_create_app_default_config():
    app = create_app()
    assert app is not None
    assert "SECRET_KEY" in app.config
    assert app.config["SECRET_KEY"] is not None


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert data["service"] == "autonomous-ai-orchestrator"


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert data["version"] == "0.1.0"
    assert data["message"] == "Autonomous AI Orchestrator API"
    assert data["docs"] == "/health"


def test_config_defaults():
    assert Config.SECRET_KEY is not None
    assert isinstance(Config.SECRET_KEY, str)
    assert Config.BASE_DIR is not None
    assert Config.DEBUG is False or Config.DEBUG is True
    assert Config.AZURE_OPENAI_DEPLOYMENT == "gpt-4o" or Config.AZURE_OPENAI_DEPLOYMENT is not None


def test_test_config_overrides():
    assert TestConfig.TESTING is True
    assert TestConfig.SECRET_KEY == "test-secret"
    assert TestConfig.DEBUG is False


def test_services_package_exists():
    assert services_doc is not None
    assert (
        "agent" in services_doc.lower() or "CrewAI" in services_doc or "LangChain" in services_doc
    )


def test_main_module_exposes_app():
    """Import main entry point and verify the Flask app is created."""
    from src.backend.app import main as main_module

    assert hasattr(main_module, "app")
    assert main_module.app is not None
    assert main_module.app.name == "src.backend.app"
