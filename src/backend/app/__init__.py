"""Flask application factory for Autonomous AI Orchestrator."""

from flask import Flask

from .config import Config
from .extensions import db


def create_app(config_class: type[Config] = Config) -> Flask:
    """Application factory.

    Args:
        config_class: Configuration class to use.

    Returns:
        Configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # SQLAlchemy
    if app.config.get("SQLALCHEMY_DATABASE_URI"):
        db.init_app(app)

    # Register blueprints
    from .routes import health_bp

    app.register_blueprint(health_bp)

    # Import models so metadata is registered (for create_all / Alembic)
    with app.app_context():
        from . import models  # noqa: F401

    return app
