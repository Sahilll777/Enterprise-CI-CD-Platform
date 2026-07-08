from flask import Blueprint, jsonify
from app.utils.response import success_response

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health_check():
    """
    Health Check Endpoint
    """

    return success_response(
    message="Health check completed successfully",
    data={
        "application": "Enterprise CI/CD Platform",
        "version": "1.0.0",
        "status": "healthy"
    }
)

@health_bp.route("/ping", methods=["GET"])
def ping():
    """
    Ping endpoint.

    Used to verify that the application is reachable.
    """

    return success_response(
        message="Ping successful",
        data={
            "response": "pong"
        }
    )