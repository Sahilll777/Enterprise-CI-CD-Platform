from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    """
    Handles authentication business logic.
    """

    @staticmethod
    def register(username, email, password):
        """
        Register a new user.
        """

        existing_username = UserRepository.get_by_username(username)

        if existing_username:
            raise ValueError("Username already exists.")

        existing_email = UserRepository.get_by_email(email)

        if existing_email:
            raise ValueError("Email already exists.")

        hashed_password = generate_password_hash(password)

        user = User(
            username=username,
            email=email,
            password_hash=hashed_password
        )

        UserRepository.create(user)

        return user

    @staticmethod
    def login(email, password):
        """
        Authenticate a user.
        """

        user = UserRepository.get_by_email(email)

        if not user:
            raise ValueError("Invalid email or password.")

        if not check_password_hash(
            user.password_hash,
            password
        ):
            raise ValueError("Invalid email or password.")

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "username": user.username,
                "email": user.email
            }
        )
        refresh_token = create_refresh_token(
    identity=str(user.id)
)
        return {
            "user": user,
            "access_token": access_token,
            "refresh_token": refresh_token
        }
    
    @staticmethod
    def get_profile(user_id):
        """
        Get the authenticated user's profile.
        """

        user = UserRepository.get_by_id(user_id)

        if not user:
           raise ValueError("User not found.")

        return user