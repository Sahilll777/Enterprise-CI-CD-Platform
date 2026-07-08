from flask import Flask, request
from app.api.v1.health import health_bp
from app.config import DevelopmentConfig
from app.logging_config import configure_logging


def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(health_bp, url_prefix="/api/v1")
    
    # Configure logger
    logger = configure_logging()

    logger.info("======================================")
    logger.info("Enterprise CI/CD Platform Started")
    logger.info("Configuration Loaded Successfully")
    logger.info("======================================")

    @app.before_request
    def before_request():
        logger.info(f"{request.method} {request.path}")

    @app.route("/")
    def home():
        logger.info("Home endpoint accessed")

        return {
            "application": app.config["APP_NAME"],
            "version": app.config["APP_VERSION"],
            "status": "Running Successfully"
        }

    return app