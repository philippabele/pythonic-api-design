from pydantic import BaseModel


class Person(BaseModel):
    name: str
    lastname: str
    age: int
