from pydantic import BaseModel


class EsLogSchema(BaseModel):
    message: str
