from fastapi import FastAPI
from src.app.api import notes, es_log
from src.app.db import database, engine, metadata
from starlette_prometheus import metrics, PrometheusMiddleware

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
app.include_router(es_log.router, prefix="/es_log", tags=["es_log"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
