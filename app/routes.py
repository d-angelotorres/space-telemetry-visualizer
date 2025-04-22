# routes.py
from flask import Blueprint, render_template
from .telemetry import get_latest_launch  # Importing our telemetry function

# Create a Blueprint object to register routes in this module
main = Blueprint('main', __name__)

# Define a route for the homepage
@main.route('/')
def index():
    print("Index route triggered")  # This should print if the route is working
    launch_data = get_latest_launch()
    print(f"Launch Data: {launch_data}")  # Check what data you're getting
    return render_template('index.html', launch=launch_data)
