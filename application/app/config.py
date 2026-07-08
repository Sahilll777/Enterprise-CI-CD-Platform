import os
from dotenv import load_dotenv

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


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = False


class ProductionConfig(Config):
    DEBUG = False