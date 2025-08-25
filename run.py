# run.py
from app import create_app

# Create an instance of the app using the app factory
app = create_app()

# Run the app only if this file is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

