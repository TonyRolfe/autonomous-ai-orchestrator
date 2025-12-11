import os
import re
import requests
from flask import jsonify, request
from datetime import datetime
from typing import Dict

from . import api_bp

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}


def sanitize_repo_name(text: str) -> str:
    """Convert epic description into a valid GitHub repository name.

    Args:
        text: Raw epic description from user.

    Returns:
        Sanitized repo name with timestamp suffix (max 100 chars).
    """
    name = re.sub(r"[^a-zA-Z0-9\-]", "-", text.lower())
    name = re.sub(r"-+", "-", name).strip("-")
    suffix = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{name[:80]}-{suffix}"[:100]


@api_bp.route("/create-repo", methods=["POST"])
def create_repo() -> tuple[Dict[str, str], int]:
    """Create a private GitHub repository based on the user's Epic description."""
    if not GITHUB_TOKEN or not GITHUB_USERNAME:
        return jsonify({"error": "GitHub credentials not configured"}), 500

    data = request.get_json(silent=True) or {}
    epic_description = data.get("epic", "").strip()
    if not epic_description:
        return jsonify({"error": "Epic description is required"}), 400

    repo_name = sanitize_repo_name(epic_description)

    url = "https://api.github.com/user/repos"
    payload = {
        "name": repo_name,
        "description": f"Epic: {epic_description}",
        "private": True,
        "auto_init": True,  # creates initial README
    }

    response = requests.post(url, headers=HEADERS, json=payload, timeout=30)

    if response.status_code == 201:
        repo_data = response.json()
        return jsonify({
            "success": True,
            "repo_url": repo_data["html_url"],
            "repo_name": repo_name,
        }), 200

    error_msg = response.json().get("message", "Unknown GitHub error")
    return jsonify({"error": error_msg}), response.status_code
