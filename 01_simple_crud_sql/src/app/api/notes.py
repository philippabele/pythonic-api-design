from typing import List
from fastapi import APIRouter, HTTPException, Path
from src.app.api import crud
from src.app.api.models import NoteDB, NoteSchema


# add router for the notes routes
router = APIRouter()


# router to get all notes
@router.get("/", response_model=List[NoteDB])
async def read_all_notes():
    # call the get_all() function declared in crud.py
    return await crud.get_all()


# router to get one specific note
@router.get("/{id}/", response_model=NoteDB)
async def read_note(
        # get the id parameter from url
    id: int = Path(..., gt=0),
):
    # get content of note
    note = await crud.get(id)
    if not note:
        # raise an exception, if specific note was not found in the database
        raise HTTPException(status_code=404, detail="Note not found")
    return note


# router to create a new note
@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await crud.post(payload)

    # build the response object, which contains the answer of the database call
    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


# router for updating a note
@router.put("/{id}/", response_model=NoteDB)
async def update_note(
    payload: NoteSchema,
    id: int = Path(..., gt=0),
):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note_id = await crud.put(id, payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


# router to delete a note
@router.delete("/{id}/", response_model=NoteDB)
async def delete_note(id: int = Path(..., gt=0)):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    await crud.delete(id)

    return note
