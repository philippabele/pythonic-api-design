from app.api import notes, es_log
from app.db import database
from fastapi import FastAPI


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(es_log.router, prefix="/es_log", tags=["es_log"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
