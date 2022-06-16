import json

from fastapi.testclient import TestClient

from src.app.main import app

# create test client
client = TestClient(app)


# test valid response for person creation
def test_person(test_app):
    test_person_data = {"name": "John", "lastname": "Doe", "age": 25}
    response_test_person = {"name": "John", "lastname": "Doe", "age": 25}

    response = test_app.post("/person", data=json.dumps(test_person_data))
    assert response.status_code == 200
    assert response.json() == response_test_person


# test invalid post request
def test_invalid_person(test_app):
    test_invalid = {"name": "John", "lastname": "Doe", "age": -40}

    response = test_app.post("/person", data=json.dumps(test_invalid))
    assert response.status_code == 400
    assert response.json()["detail"] == "Wrong input! Set an age > 0"


# test valid response for person creation
def test_person_pydantic(test_app):
    test_person_data = {"name": "John", "lastname": "Doe", "age": 25}
    response_test_person = {"name": "John", "lastname": "Doe", "age": 25}

    response = test_app.post("/pydantic_person", data=json.dumps(test_person_data))
    assert response.status_code == 200
    assert response.json() == response_test_person


# test invalid post request
def test_invalid_person_pydantic(test_app):
    test_invalid = {"name": "John", "lastname": "Doe", "age": -40}

    response = test_app.post("/pydantic_person", data=json.dumps(test_invalid))
    assert response.status_code == 400
    assert response.json()["detail"] == "Wrong input! Set an age > 0"

