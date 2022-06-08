from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from src.app.routers import notes, pets
from src.app.db import database, engine, metadata

# create database schema
metadata.create_all(engine)

tags_metadata = [
    {"name": "notes", "description": "Store your notes"},
    {"name": "petstore", "description": "This is a pet store."},
]
# create FastAPI application
app = FastAPI(title="Simple CRUD SQL", openapi_tags=tags_metadata)


# start database
@app.on_event("startup")
async def startup():
    await database.connect()


# stop database
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.exception_handler(StarletteHTTPException)
def not_found_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": exc.detail}
    )


@app.exception_handler(RequestValidationError)
def relation_not_found_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": exc}
    )


# include FastAPI routers for notes & pets, which are defined in other files
app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(pets.router, prefix="/petstore", tags=["petstore"])


# root route, which is shown if the API is called
@app.get("/")
async def root():
    return {"message": "Hello World"}
