from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health_check():
    """
    Health Check Endpoint
    """

    return jsonify(
        {
            "status": "healthy",
            "application": "Enterprise CI/CD Platform",
            "version": "1.0.0"
        }
    ), 200