from pydantic import BaseModel, Field


# declare schemas here, each declares the structure of an object

# model NoteSchema has two attributes: title and description
class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)


class NoteDB(NoteSchema):
    id: int
