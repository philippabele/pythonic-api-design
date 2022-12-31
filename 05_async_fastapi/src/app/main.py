import time
from fastapi import FastAPI, Request
from src.app.api import recipes_router

# create FastAPI application
app = FastAPI(title="Async FastAPI")


# add middleware to track processing time of requests
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# include FastAPI router for notes, which is defined in another file
app.include_router(recipes_router.router, prefix="/ideas", tags=["recipes"])


# root route, which is shown if the API is called
@app.get("/")
async def root():
    return {"message": "Hello World"}
