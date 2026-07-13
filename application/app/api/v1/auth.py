from flask import Blueprint

from app.controllers.auth_controller import AuthController

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route(
    "/register",
    methods=["POST"]
)
def register():
    """
    Register a new user.
    ---
    tags:
      - Authentication

    consumes:
      - application/json

    produces:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - email
            - password
          properties:
            username:
              type: string
              example: sahil
            email:
              type: string
              example: sahil@example.com
            password:
              type: string
              example: Password@123

    responses:
      201:
        description: User registered successfully.

      400:
        description: Validation error.

      500:
        description: Internal server error.
    """

    return AuthController.register()

@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():
    """
    Authenticate an existing user.
    ---
    tags:
      - Authentication

    consumes:
      - application/json

    produces:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: sahil@example.com
            password:
              type: string
              example: Password@123

    responses:
      200:
        description: Login successful.

      401:
        description: Invalid credentials.

      500:
        description: Internal server error.
    """

    return AuthController.login()

@auth_bp.route(
    "/profile",
    methods=["GET"]
)
def profile():
    """
    Get authenticated user profile.
    ---
    tags:
      - Authentication

    security:
      - Bearer: []

    responses:
      200:
        description: Profile retrieved successfully.

      401:
        description: Authentication required.
    """

    return AuthController.profile()

@auth_bp.route(
    "/refresh",
    methods=["POST"]
)
def refresh():
    return AuthController.refresh()

@auth_bp.route(
    "/admin",
    methods=["GET"]
)
def admin_dashboard():
    """
    Admin Dashboard.
    ---
    tags:
      - Authentication

    security:
      - Bearer: []

    responses:
      200:
        description: Admin dashboard.

      403:
        description: Forbidden.
    """

    return AuthController.admin_dashboard()