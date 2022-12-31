from src.app.db import notes, database

from .models import NoteSchema


# these functions interact with the database and are executed, if their corresponding FastAPI route is called

# declare notes post route: insert a new note
async def post(payload: NoteSchema):
    # build a sql query
    query = notes.insert().values(title=payload.title, description=payload.description)
    # return the answer of the database execution
    return await database.execute(query=query)


# get a specific note
async def get(id: int):
    query = notes.select().where(id == notes.c.id)
    return await database.fetch_one(query=query)


# get all notes
async def get_all():
    query = notes.select()
    return await database.fetch_all(query=query)


# modify/change an existing note
async def put(id: int, payload: NoteSchema):
    query = (
        notes.update()
        .where(id == notes.c.id)
        .values(title=payload.title, description=payload.description)
        .returning(notes.c.id)
    )
    return await database.execute(query=query)


# delete a specific note
async def delete(id: int):
    query = notes.delete().where(id == notes.c.id)
    return await database.execute(query=query)
