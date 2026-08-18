"""Tests for SQLAlchemy models and database initialization."""

import pytest

from src.backend.app import create_app
from src.backend.app.config import TestConfig
from src.backend.app.extensions import db
from src.backend.app.models import Conversation, GitHubCredential, Session, User


@pytest.fixture
def app():
    application = create_app(TestConfig)
    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_db_extension_initialized(app):
    assert db.engine is not None
    assert "sqlite" in str(db.engine.url)


def test_user_model_create_and_query(app):
    user = User(email="alice@example.com", password_hash="hashed")
    db.session.add(user)
    db.session.commit()

    found = db.session.scalar(db.select(User).where(User.email == "alice@example.com"))
    assert found is not None
    assert found.email == "alice@example.com"
    assert found.id is not None
    assert repr(found).startswith("<User ")


def test_github_credential_relationship(app):
    user = User(email="bob@example.com", password_hash="hashed")
    db.session.add(user)
    db.session.flush()

    cred = GitHubCredential(
        user_id=user.id,
        encrypted_pat="gAAAAABencrypted-token-placeholder",
        target_org="my-org",
    )
    db.session.add(cred)
    db.session.commit()

    assert len(user.github_credentials) == 1
    assert user.github_credentials[0].target_org == "my-org"
    assert repr(cred).startswith("<GitHubCredential ")


def test_session_model(app):
    user = User(email="carol@example.com", password_hash="hashed")
    db.session.add(user)
    db.session.flush()

    from datetime import datetime, timedelta, timezone

    sess = Session(
        user_id=user.id,
        session_token="tok-abc-123",
        expires_at=datetime.now(timezone.utc) + timedelta(days=7),
    )
    db.session.add(sess)
    db.session.commit()

    assert len(user.sessions) == 1
    assert user.sessions[0].session_token == "tok-abc-123"
    assert repr(sess).startswith("<Session ")


def test_conversation_model(app):
    user = User(email="dave@example.com", password_hash="hashed")
    db.session.add(user)
    db.session.flush()

    conv = Conversation(
        user_id=user.id,
        title="Epic: Shipping Portal",
        epic_text="Build a domestic shipping form...",
        status="active",
    )
    db.session.add(conv)
    db.session.commit()

    assert len(user.conversations) == 1
    assert user.conversations[0].title == "Epic: Shipping Portal"
    assert repr(conv).startswith("<Conversation ")


def test_cascade_delete_user(app):
    user = User(email="eve@example.com", password_hash="hashed")
    db.session.add(user)
    db.session.flush()

    from datetime import datetime, timedelta, timezone

    db.session.add(
        GitHubCredential(user_id=user.id, encrypted_pat="enc", target_org=None)
    )
    db.session.add(
        Session(
            user_id=user.id,
            session_token="tok-xyz",
            expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
        )
    )
    db.session.add(Conversation(user_id=user.id, title="T", status="active"))
    db.session.commit()

    user_id = user.id
    db.session.delete(user)
    db.session.commit()

    assert db.session.get(User, user_id) is None
    assert db.session.scalars(db.select(GitHubCredential)).all() == []
    assert db.session.scalars(db.select(Session)).all() == []
    assert db.session.scalars(db.select(Conversation)).all() == []
