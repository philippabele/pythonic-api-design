from typing import List, Any

from src.app.db import petstore, database
from src.app.models.pet import PetSchema


# these functions interact with the database and are executed, if their corresponding FastAPI route is called

class PetSchemaDb:
    id: int
    category_id: int
    category_name: str
    name: str
    status: str


def parse_database_response(resp: List[PetSchemaDb]):
    temp_list: List[PetSchema] = []
    for element in resp:
        temp_obj: PetSchema = {
            "id": element.id,
            "category": {
                "id": element.category_id,
                "name": element.category_name
            },
            "name": element.name,
            "status": element.status
        }
        temp_list.append(temp_obj)
    return temp_list


# declare notes post route: insert a new note
async def post(payload: PetSchema):
    # build a sql query
    query = petstore.insert().values(name=payload.name, status=payload.status, category_id=payload.category.id,
                                     category_name=payload.category.name)
    # return the answer of the database execution
    return await database.execute(query=query)


# declare notes post route: insert a new note
async def update(payload: PetSchema):
    # build a sql query
    query = petstore.update().where(payload.id == petstore.c.id).values(name=payload.name, status=payload.status, category_id=payload.category.id,
                                     category_name=payload.category.name).returning(petstore.c.id)
    # return the answer of the database execution
    resp = await database.execute(query=query)
    return resp


# declare notes post route: insert a new note
async def update_fields(petId: int, name: str, status: str):
    # build a sql query
    query = petstore.update().where(petId == petstore.c.id).values(name=name, status=status).returning(petstore.c.id)
    # return the answer of the database execution
    return await database.execute(query=query)


# get a specific note
async def get(id: int):
    query = petstore.select().where(id == petstore.c.id)
    resp = await database.fetch_one(query=query)
    if resp:
        temp_obj: PetSchema = {
            "id": resp.id,
            "category": {
                "id": resp.category_id,
                "name": resp.category_name
            },
            "name": resp.name,
            "status": resp.status
        }
        return temp_obj
    else:
        return resp


# get all notes
async def get_by_status(status: str):
    query = petstore.select().where(status == petstore.c.status)
    resp = await database.fetch_all(query=query)
    if resp:
        return parse_database_response(resp)
    else:
        return resp


# modify/change an existing note
async def put(payload: PetSchema):
    query = (
        petstore.update()
        .where(id == petstore.c.id)
        .values(name=payload.name, status=payload.status, category_id=payload.category.id,
                category_name=payload.category.name)
        .returning(petstore.c.id)
    )
    return await database.execute(query=query)


# delete a specific note
async def delete(pet_id: int):
    query = petstore.delete().where(pet_id == petstore.c.id)
    return await database.execute(query=query)
