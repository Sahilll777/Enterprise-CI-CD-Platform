from flask import request

from app.services.auth_service import AuthService
from app.utils.response import success_response, error_response


class AuthController:
    """
    Handles authentication HTTP requests.
    """

    @staticmethod
    def register():
        data = request.get_json()

        if not data:
            return error_response(
                message="Request body must be JSON.",
                status_code=400
            )

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return error_response(
                message="Missing required fields.",
                errors=[
                    "username, email and password are required."
                ],
                status_code=400
            )

        try:
            user = AuthService.register(
                username=username,
                email=email,
                password=password
            )

            return success_response(
                message="User registered successfully.",
                data={
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                status_code=201
            )

        except ValueError as error:
            return error_response(
                message=str(error),
                status_code=400
            )

        except Exception:
            return error_response(
                message="Registration failed.",
                status_code=500
            )

    @staticmethod
    def login():
        """
        Authenticate an existing user.
        """

        data = request.get_json()

        if not data:
            return error_response(
                message="Request body must be JSON.",
                status_code=400
            )

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return error_response(
                message="Missing required fields.",
                errors=[
                    "email and password are required."
                ],
                status_code=400
            )

        try:
            user = AuthService.login(
                email=email,
                password=password
            )

            return success_response(
                message="Login successful.",
                data={
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                status_code=200
            )

        except ValueError as error:
            return error_response(
                message=str(error),
                status_code=401
            )

        except Exception:
            return error_response(
                message="Login failed.",
                status_code=500
            )