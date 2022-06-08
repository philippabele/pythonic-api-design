from typing import List, Any

from fastapi import APIRouter, HTTPException, Path, UploadFile
from src.app.api import crud_pets
from src.app.models.pet import PetDB, PetSchema, PetStatus, UpdatePet


# add router for the petstore routes
router = APIRouter()


# router to get all pets by their status
@router.get(
    "/findByStatus", response_model=List[PetSchema], description="Find pet by status"
)
async def get_pet_by_status(status: PetStatus):
    # call the get_all() function declared in crud_pets.py
    if status == PetStatus.available:
        return await crud_pets.get_by_status("available")
    elif status == PetStatus.pending:
        return await crud_pets.get_by_status("pending")
    elif status == PetStatus.sold:
        return await crud_pets.get_by_status("sold")
    else:
        raise HTTPException(status_code=404, detail="Status not found")


# router to get one specific pet
@router.get("/{petId}", response_model=Any, summary="Get a pet by ID")
async def read_pet(
    # get the id parameter from url
    petId: int = Path(..., gt=0),
):
    # get content of pet
    pet = await crud_pets.get(petId)
    if not pet:
        # raise an exception, if specific pet was not found in the database
        raise HTTPException(status_code=404, detail="pet not found")
    return pet


# router to create a new pet
@router.post(
    "/",
    response_model=PetSchema,
    status_code=201,
    description="Add a new pet to the store",
)
async def create_pet(payload: PetSchema):
    pet_id = await crud_pets.post(payload)

    # build the response object, which contains the answer of the database call
    response_object = {
        "id": pet_id,
        "category": {"id": payload.category.id, "name": payload.category.name},
        "name": payload.name,
        "status": payload.status,
    }
    return response_object


@router.post(
    "/{petId}",
    response_model=UpdatePet,
    status_code=201,
    description="Updates a pet in the store with form data",
)
async def update_pet_form(petId: int, name: str, status: str):
    # async def update_pet_form(petId: int = Query(None, description="Update pets id"),
    #                           name: str = Query(None, description="Type the new name"),
    #                           status: str = Query(None, description="Set new status")):

    db_response = await crud_pets.update_fields(petId, name, status)
    print(db_response)
    if not db_response:
        # raise an exception, if specific pet was not found in the database
        raise HTTPException(status_code=404, detail="Pet not updated")

    # build the response object, which contains the answer of the database call
    response_object = {
        "id": db_response,
        "name": name,
        "status": status,
    }
    return response_object


# router for updating a pet
@router.put("/", response_model=PetDB)
async def update_pet(payload: PetSchema):
    pet_id = await crud_pets.update(payload)

    if not pet_id:
        raise HTTPException(status_code=404, detail="Pet not found")

    response_object = {"id": pet_id}
    return response_object


# router to delete a pet
@router.delete("/{petId}", response_model=PetSchema)
async def delete_pet(petId: int = Path(..., gt=0, description="Pet id to delete")):
    pet = await crud_pets.get(petId)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    await crud_pets.delete(petId)

    return pet
