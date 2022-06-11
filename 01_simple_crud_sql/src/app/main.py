from fastapi import FastAPI
from src.app.routers import notes, pets
from src.app.db import database, engine, metadata

# create database schema
metadata.create_all(engine)

tags_metadata = [
    {"name": "notes", "description": "Store your notes"},
    {"name": "petstore", "description": "This is a pet store."},
]
# create FastAPI application
app = FastAPI(title="Simple CRUD SQL", openapi_tags=tags_metadata)


# start database
@app.on_event("startup")
async def startup():
    await database.connect()


# stop database
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# include FastAPI routers for notes & pets, which are defined in other files
app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(pets.router, prefix="/petstore", tags=["petstore"])


# root route, which is shown if the API is called
@app.get("/")
async def root():
    return {"message": "Hello World"}
