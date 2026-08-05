"""Flask application factory for Autonomous AI Orchestrator."""

from flask import Flask

from .config import Config


def create_app(config_class: type[Config] = Config) -> Flask:
    """Application factory.

    Args:
        config_class: Configuration class to use.

    Returns:
        Configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    from .routes import health_bp

    app.register_blueprint(health_bp)

    return app
