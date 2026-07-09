from functools import wraps

from flask_jwt_extended import get_jwt

from app.utils.response import error_response


def roles_required(*allowed_roles):
    """
    Restrict endpoint access to specific roles.
    """

    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):

            claims = get_jwt()

            user_role = claims.get("role")

            if user_role not in allowed_roles:

                return error_response(
                    message="Access denied. Insufficient permissions.",
                    status_code=403
                )

            return fn(*args, **kwargs)

        return wrapper

    return decorator