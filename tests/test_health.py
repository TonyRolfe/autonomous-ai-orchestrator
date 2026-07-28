"""Tests for health and root endpoints."""

import pytest
from src.backend.app import create_app
from src.backend.app.config import TestConfig


@pytest.fixture
def client():
    app = create_app(TestConfig)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


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
