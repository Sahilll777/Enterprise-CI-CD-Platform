from flask import jsonify


def register_error_handlers(app):
    """
    Register global error handlers.
    """

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "message": "Bad Request",
            "errors": ["The request could not be processed."]
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "message": "Unauthorized",
            "errors": ["Authentication is required."]
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "message": "Forbidden",
            "errors": ["Access denied."]
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "message": "Resource Not Found",
            "errors": ["The requested endpoint does not exist."]
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "message": "Method Not Allowed",
            "errors": ["This HTTP method is not allowed."]
        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "message": "Internal Server Error",
            "errors": ["Something went wrong on the server."]
        }), 500