from flask import Blueprint

from app.controllers.user_controller import UserController

users_bp = Blueprint(
    "users",
    __name__
)


@users_bp.route(
    "",
    methods=["GET"]
)
def get_all_users():
    return UserController.get_all_users()