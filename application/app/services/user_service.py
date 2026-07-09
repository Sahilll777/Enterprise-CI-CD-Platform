from app.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash
from app.models.user import User


class UserService:
    """
    Handles user management business logic.
    """

    @staticmethod
    def get_users(page, per_page, search=None, role=None):
        return UserRepository.get_users(
            page,
            per_page,
            search,
            role
        )

    @staticmethod
    def create_user(
        username,
        email,
        password,
        role
    ):
        """
        Create a user from the admin panel.
        """

        if UserRepository.get_by_username(username):
            raise ValueError("Username already exists.")

        if UserRepository.get_by_email(email):
            raise ValueError("Email already exists.")

        role = role.upper()

        if role not in [
            "ADMIN",
            "USER"
        ]:
            raise ValueError("Invalid role.")

        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            role=role
        )

        return UserRepository.create(user)

    @staticmethod
    def get_user(user_id):
        """
        Retrieve a single user by ID.
        """

        user = UserRepository.get_by_id(user_id)

        if not user:
            raise ValueError("User not found.")

        return user