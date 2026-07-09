from flask import request
from flask_jwt_extended import jwt_required
from app.decorators.roles import roles_required
from app.services.user_service import UserService
from app.utils.response import success_response, error_response

class UserController:
    """
    Handles user management HTTP requests.
    """

    @staticmethod
    @jwt_required()
    @roles_required("ADMIN")
    def get_all_users():

        page = request.args.get("page", default=1, type=int)

        per_page = request.args.get("per_page", default=10, type=int)

        search = request.args.get("search")

        role = request.args.get("role")

        users = UserService.get_users(
            page=page,
            per_page=per_page,
            search=search,
            role=role
        )

        return success_response(
            message="Users retrieved successfully.",
            data={
                "users": [
                    {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "role": user.role
                    }
                    for user in users.items
                ],
                "pagination": {
                    "page": users.page,
                    "per_page": users.per_page,
                    "total_records": users.total,
                    "total_pages": users.pages
                }
            }
        )

    @staticmethod
    @jwt_required()
    @roles_required("ADMIN")
    def create_user():

        data = request.get_json()

        if not data:
            return error_response(
                message="Request body must be JSON.",
                status_code=400
            )

        required = [
            "username",
            "email",
            "password",
            "role"
        ]

        for field in required:
            if not data.get(field):
                return error_response(
                    message=f"{field} is required.",
                    status_code=400
                )

        try:
            user = UserService.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
                role=data["role"]
            )

            return success_response(
                message="User created successfully.",
                data={
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                },
                status_code=201
            )

        except ValueError as error:
            return error_response(
                message=str(error),
                status_code=400
            )

    @staticmethod
    @jwt_required()
    @roles_required("ADMIN")
    def get_user(user_id):
        """
        Return one user.
        """
        try:
            user = UserService.get_user(user_id)

            return success_response(
                message="User retrieved successfully.",
                data={
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                }
            )

        except ValueError as error:
            return error_response(
                message=str(error),
                status_code=404
            )