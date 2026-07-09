from flask import Flask, request
from app.api.v1.health import health_bp
from app.config import DevelopmentConfig
from app.logging_config import configure_logging
from app.error_handlers import register_error_handlers
from app.extensions import db, migrate
from app.models import User
from app.api.v1.auth import auth_bp
from app.extensions import db, migrate, jwt
from app.jwt_handlers import register_jwt_handlers

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(health_bp, url_prefix="/api/v1")
    app.register_blueprint(
    auth_bp,
    url_prefix="/api/v1/auth"
)
    register_error_handlers(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    migrate.init_app(app, db)
    register_jwt_handlers(jwt)
    
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