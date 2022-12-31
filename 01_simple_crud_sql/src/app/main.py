from fastapi import FastAPI
from src.app.api import notes
from src.app.db import database, engine, metadata

# create database schema
metadata.create_all(engine)


# create FastAPI application
app = FastAPI()


# start database
@app.on_event("startup")
async def startup():
    await database.connect()


# stop database
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# include FastAPI router for notes, which is defined in another file
app.include_router(notes.router, prefix="/notes", tags=["notes"])


# root route, which is shown if the API is called
@app.get("/")
async def root():
    return {"message": "Hello World"}
