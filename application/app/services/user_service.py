from app.repositories.user_repository import UserRepository


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