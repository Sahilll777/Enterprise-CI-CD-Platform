import os
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables from the .env file
load_dotenv()


class Config:
    """
    Base configuration for the application.
    """

    SECRET_KEY = os.getenv("SECRET_KEY")

    APP_NAME = os.getenv("APP_NAME")

    APP_VERSION = os.getenv("APP_VERSION")

    DEBUG = os.getenv("FLASK_DEBUG") == "True"

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

    DATABASE_HOST = os.getenv("DATABASE_HOST")

    DATABASE_PORT = os.getenv("DATABASE_PORT")

    DATABASE_NAME = os.getenv("DATABASE_NAME")

    DATABASE_USER = os.getenv("DATABASE_USER")

    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

    SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}"
    f"/{DATABASE_NAME}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

JWT_ACCESS_TOKEN_EXPIRES = timedelta(
    minutes=int(
        os.getenv(
            "JWT_ACCESS_TOKEN_EXPIRES",
            30
        )
    )
)

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = False


class ProductionConfig(Config):
    DEBUG = False