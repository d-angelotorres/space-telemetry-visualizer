from flask import Flask


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)

    from .routes import main  # Import blueprint

    app.register_blueprint(main)

    return app
