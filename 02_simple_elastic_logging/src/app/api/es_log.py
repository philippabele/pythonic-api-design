from datetime import datetime

from fastapi import APIRouter
from src.app.api.models import EsLogSchema
from src.app.elasticsearch import ESClient

esclient = ESClient()
esclient.startup()

router = APIRouter()


def es_post_log(document: dict):
    response = esclient.es.index(index="logging", document=document)
    return response


@router.post("/es-log", status_code=201)
async def es_log(payload: EsLogSchema):
    document = {
        "route": "/es-log",
        "message": payload.message,
        "timestamp": datetime.now(),
    }
    resp = es_post_log(document)
    return resp
