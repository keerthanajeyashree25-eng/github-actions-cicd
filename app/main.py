"""A small Flask application used by the CI/CD example."""

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    """Return a welcome message."""
    return jsonify(message="Welcome to the Flask CI/CD demo!")


@app.get("/health")
def health():
    """Report that the application is running."""
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
