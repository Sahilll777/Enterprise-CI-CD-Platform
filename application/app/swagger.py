from flasgger import Swagger


def configure_swagger(app):
    """
    Configure Swagger UI.
    """

    template = {
        "swagger": "2.0",
        "info": {
            "title": "Enterprise CI/CD Platform API",
            "description": "Enterprise Flask REST API with JWT Authentication",
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": (
                    "JWT Authorization header.\n\n"
                    "Example:\n"
                    "Bearer eyJhbGciOiJIUzI1NiIs..."
                )
            }
        }
    }

    Swagger(
        app,
        template=template
    )