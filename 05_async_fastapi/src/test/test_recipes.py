from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_get_ideas(test_app):
    response = test_app.get("/ideas/")
    assert response.status_code == 200
    keys = response.json().keys()
    assert "recipes" in keys
    assert "easyRecipes", "topSecretRecipes" in keys


def test_get_ideas_async(test_app):
    response = test_app.get("/ideas/async")
    assert response.status_code == 200
    keys = response.json().keys()
    assert "recipes" in keys
    assert "easyRecipes", "topSecretRecipes" in keys
