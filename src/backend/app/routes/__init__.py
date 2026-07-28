"""Route blueprints."""

from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health_check() -> tuple[dict, int]:
    """Health check endpoint for readiness/liveness probes."""
    return jsonify({"status": "ok", "service": "autonomous-ai-orchestrator"}), 200


@health_bp.route("/", methods=["GET"])
def root() -> tuple[dict, int]:
    """Root endpoint."""
    return (
        jsonify(
            {
                "message": "Autonomous AI Orchestrator API",
                "version": "0.1.0",
                "docs": "/health",
            }
        ),
        200,
    )
