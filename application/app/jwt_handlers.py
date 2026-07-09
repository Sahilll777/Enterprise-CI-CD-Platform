from flask_jwt_extended import JWTManager

from app.utils.response import error_response


def register_jwt_handlers(jwt: JWTManager):
    """
    Register custom JWT callbacks.
    """

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return error_response(
            message="Access token has expired.",
            status_code=401
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return error_response(
            message="Invalid access token.",
            status_code=401
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return error_response(
            message="Authentication required.",
            status_code=401
        )

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return error_response(
            message="Access token has been revoked.",
            status_code=401
        )

    @jwt.needs_fresh_token_loader
    def fresh_token_callback(jwt_header, jwt_payload):
        return error_response(
            message="Fresh login required.",
            status_code=401
        )