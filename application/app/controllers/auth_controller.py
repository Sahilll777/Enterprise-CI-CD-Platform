from flask import request
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token
)

from app.services.auth_service import AuthService
from app.utils.response import success_response, error_response


class AuthController:
    """
    Handles authentication HTTP requests.
    """

    @staticmethod
    def register():
        """
        Register a new user.
        """

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
            result = AuthService.login(
                email=email,
                password=password
            )

            user = result["user"]
            access_token = result["access_token"]
            refresh_token = result["refresh_token"]

            return success_response(
                message="Login successful.",
                data={
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email
                    }
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

    @staticmethod
    @jwt_required()
    def profile():
        """
        Return the authenticated user's profile.
        """

        try:
            user_id = get_jwt_identity()

            user = AuthService.get_profile(user_id)

            return success_response(
                message="Profile retrieved successfully.",
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
                status_code=404
            )

        except Exception:
            return error_response(
                message="Failed to retrieve profile.",
                status_code=500
            )

    @staticmethod
    @jwt_required(refresh=True)
    def refresh():
        """
        Generate a new access token using a refresh token.
        """

        user_id = get_jwt_identity()

        access_token = create_access_token(
            identity=user_id
        )

        return success_response(
            message="Access token refreshed successfully.",
            data={
                "access_token": access_token
            },
            status_code=200
        )