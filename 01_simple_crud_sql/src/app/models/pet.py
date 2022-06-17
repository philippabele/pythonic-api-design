from enum import Enum

from pydantic import BaseModel, Field
from typing import List

# declare schemas here, each declares the structure of an object


# model PetCategory has two attributes: id & name, where name is limited to a length of 50 chars
class PetCategory(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50)


class PetSchema(BaseModel):
    id: int
    category: PetCategory
    name: str = Field(..., min_length=3, max_length=50)
    status: str = Field(..., min_length=3, max_length=50)


class PetDB(BaseModel):
    id: int


#  create enum for status of pets
class PetStatus(str, Enum):
    available = "available"
    pending = "pending"
    sold = "sold"


class UpdatePet(BaseModel):
    id: int
    name: str
    status: str
