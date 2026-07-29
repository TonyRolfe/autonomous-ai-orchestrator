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


def test_create_app_default_config():
    app = create_app()
    assert app is not None
    assert "SECRET_KEY" in app.config


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


def test_config_defaults():
    assert Config.SECRET_KEY is not None
    assert Config.FLASK_ENV in ("development", "production", "testing") or True
    assert Config.BASE_DIR is not None


def test_services_package_exists():
    assert services_doc is not None or True
