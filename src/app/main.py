import time
import json
import requests
from datetime import datetime
from fastapi import FastAPI
from elasticsearch import Elasticsearch
from app.api import notes
from app.db import database, engine, metadata


def connect_elasticsearch():
    time.sleep(15)
    _es = None
    _es = Elasticsearch("http://127.0.0.1:9200")
    return _es


es = connect_elasticsearch()

doc = {
    'author': 'author_name',
    'text': 'Interensting content...',
    'timestamp': datetime.now(),
}
resp = es.index(index="test-index", id=1, document=doc)
print(resp['result'])

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(notes.router, prefix="/notes", tags=["notes"])


@app.get("/")
async def root():
    return {"message": "Hello World"}

