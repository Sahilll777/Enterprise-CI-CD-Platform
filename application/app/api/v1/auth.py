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
    """

    return AuthController.register()

@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():
    """
    Authenticate an existing user.
    """

    return AuthController.login()