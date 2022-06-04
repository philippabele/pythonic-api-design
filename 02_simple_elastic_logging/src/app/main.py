from fastapi import FastAPI
from src.app.api import es_log

app = FastAPI()

app.include_router(es_log.router, prefix="/es_log", tags=["es_log"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
