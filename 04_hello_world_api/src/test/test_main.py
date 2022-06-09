from fastapi.testclient import TestClient

from src.app.main import app

# create test client
client = TestClient(app)


# test root function
def test_read_main(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


# test valid response for int
def test_sqrt(test_app):
    response = test_app.get("/sqrt/25")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


# test valid response for float
def test_sqrt_float(test_app):
    response = test_app.get("/sqrt/0.25")
    assert response.status_code == 200
    assert response.json() == {"result": 0.5}


# test error response for string
def test_sqrt_error(test_app):
    response = test_app.get("/sqrt/number")
    assert response.status_code == 422


# test error response for number, which is less than zero
def test_sqrt_error_validation(test_app):
    response = test_app.get("/sqrt/-9")
    assert response.status_code == 400
    assert response.json() == {"detail": "Wrong input"}
