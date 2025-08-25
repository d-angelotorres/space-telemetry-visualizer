from flask import Blueprint, render_template
from .telemetry import get_latest_launch  # Import telemetry function

# Blueprint setup
main = Blueprint("main", __name__)


@main.route("/")
def index():
    """Render homepage with latest launch data."""
    print("Index route triggered")
    launch_data = get_latest_launch()
    print(f"Launch Data: {launch_data}")
    return render_template("index.html", launch=launch_data)
