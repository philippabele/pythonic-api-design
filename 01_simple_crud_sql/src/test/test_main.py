from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_read_main(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
