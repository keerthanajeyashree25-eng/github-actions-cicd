"""Tests for the Flask application's HTTP routes."""

from app.main import app


def test_home_returns_welcome_message():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {
        "message": "Welcome to the Flask CI/CD demo!"
    }


def test_health_returns_healthy_status():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"status": "healthy"}
