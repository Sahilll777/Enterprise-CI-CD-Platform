from flask import Blueprint

from app.controllers.user_controller import UserController

users_bp = Blueprint(
    "users",
    __name__
)