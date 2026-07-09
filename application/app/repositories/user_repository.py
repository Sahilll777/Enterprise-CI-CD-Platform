from app.extensions import db
from app.models.user import User


class UserRepository:
    """
    Handles all database operations
    related to the User model.
    """

    @staticmethod
    def get_by_id(user_id):
        return db.session.get(User, user_id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def get_users(page, per_page, search=None, role=None):
        query = User.query

        if search:
            query = query.filter(
                db.or_(
                    User.username.ilike(f"%{search}%"),
                    User.email.ilike(f"%{search}%")
                )
            )

        if role:
            query = query.filter(
                User.role == role.upper()
            )

        return query.order_by(User.id.asc()).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )