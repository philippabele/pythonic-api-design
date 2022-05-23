from fastapi import FastAPI
from starlette_prometheus import metrics, PrometheusMiddleware
from app.api import notes
from app.db import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", metrics)


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

