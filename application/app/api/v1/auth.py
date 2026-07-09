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

@auth_bp.route(
    "/profile",
    methods=["GET"]
)
def profile():
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
    return AuthController.admin_dashboard()