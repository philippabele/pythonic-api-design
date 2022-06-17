from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from src.app.api.person import Person

# create FastAPI application
app = FastAPI()


# simple route to create a person manually
@app.post(
    "/person",
    summary="Create a person manually",
    description="fill in each field",
)
async def post_person(name: str, lastname: str, age: int) -> dict:
    if age < 0:
        raise HTTPException(status_code=400, detail="Wrong input! Set an age > 0")
    return {"name": name, "lastname": lastname, "age": age}


# simple route to create a person by model
@app.post(
    "/pydantic_person",
    summary="Create a Person model",
    description="Match your values with the provided keys",
)
async def pydantic_post_person(person: Person) -> dict:  # set the Person model as input
    if person.age < 0:
        raise HTTPException(status_code=400, detail="Wrong input! Set an age > 0")
    json_person = jsonable_encoder(person)  # encode model to json for response
    return json_person
