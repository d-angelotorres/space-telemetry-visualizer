# app/__init__.py
from flask import Flask

def create_app():
    # Create a Flask app instance
    app = Flask(__name__)

    # Import the blueprint from routes.py
    from .routes import main

    # Register the blueprint with the app
    app.register_blueprint(main)

    return app
