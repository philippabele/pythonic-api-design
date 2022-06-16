import json

import pytest
from src.app.api import crud_pets


# testing create pet
def test_create_pet(test_app, monkeypatch):
    test_request_payload = {
        "id": 1,
        "category": {"id": 1, "name": "cat"},
        "name": "Citty",
        "status": "available",
    }
    test_response_payload = {
        "id": 1,
        "category": {"id": 1, "name": "cat"},
        "name": "Citty",
        "status": "available",
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud_pets, "post", mock_post)

    response = test_app.post(
        "/petstore/",
        data=json.dumps(test_request_payload),
    )

    assert response.status_code == 201
    assert response.json() == test_response_payload


# test invalid response, missing id
def test_create_pet_invalid_json(test_app):
    response = test_app.post("/petstore/", data=json.dumps({"name": "somebody"}))
    assert response.status_code == 422

    response = test_app.post(
        "/petstore/", data=json.dumps({"name": "somebody", "status": "pending"})
    )
    assert response.status_code == 422


# test reading pet
def test_read_pet(test_app, monkeypatch):
    test_response_payload = {
        "id": 1,
        "category": {"id": 1, "name": "cat"},
        "name": "Citty",
        "status": "available",
    }

    async def mock_get(id):
        return test_response_payload

    response = test_app.get("/petstore/1")
    assert response.status_code == 200
    assert response.json() == test_response_payload


# test reading pet with not available id
def test_read_pet_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud_pets, "get", mock_get)

    response = test_app.get("/petstore/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "pet not found"

    response = test_app.get("/petstore/1")
    assert response.status_code == 404


# test reading all pets
def test_read_pet_by_status(test_app, monkeypatch):
    test_read_status = {"status": "available"}
    test_data_status = [
        {
            "id": 1,
            "category": {"id": 1, "name": "cat"},
            "name": "Citty",
            "status": "available",
        }
    ]

    async def mock_get_all(*args, **kwargs):
        return None

    monkeypatch.setattr(crud_pets, "get_by_status", mock_get_all)

    response = test_app.get("/petstore/findByStatus?status=available")
    assert response.status_code == 200
    assert response.json() == test_data_status


# test updating existing pet
def test_update_pet(test_app, monkeypatch):
    test_update_data = {
        "id": 1,
        "name": "Citty",
        "status": "pending",
        "category": {"id": 1, "name": "cat"},
    }

    async def mock_get(id):
        return True

    monkeypatch.setattr(crud_pets, "get", mock_get)

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(crud_pets, "put", mock_put)

    response = test_app.put("/petstore/", data=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == {"id": 1}


@pytest.mark.parametrize(
    "payload, status_code",
    [
        [{}, 422],
        [
            {
                "id": 5,
                "category": {"id": 0, "name": "dog"},
                "name": "Puppy",
                "status": "available",
            },
            422,
        ],
        [{"id": 999, "category": {"id": 0, "name": "dog"}, "status": "available"}, 422],
        [{"id": 5, "name": "Puppy", "status": "available"}, 422],
        [{"id": 5, "category": {"id": 0, "name": "dog"}, "name": "Puppy"}, 422],
        [
            {
                "category": {"id": 0, "name": "dog"},
                "name": "Puppy",
                "status": "available",
            },
            422,
        ],
    ],
)
# test updating pet with statements that should fail
def test_update_pet_invalid(test_app, monkeypatch, payload, status_code):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud_pets, "get", mock_get)

    response = test_app.put(
        f"/petstore/",
        data=json.dumps(payload),
    )
    assert response.status_code == status_code


# test removing specific pet
def test_remove_pet(test_app, monkeypatch):
    test_data = {"id": 1}

    async def mock_delete(id):
        return id

    monkeypatch.setattr(crud_pets, "delete", mock_delete)

    response = test_app.delete("/petstore/1/")
    assert response.status_code == 200
    assert response.json() == test_data


# test deleting pet with not available id
def test_remove_pet_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud_pets, "delete", mock_get)

    response = test_app.delete("/petstore/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "pet not found"

    response = test_app.delete("/petstore/1/")
    assert response.status_code == 422
