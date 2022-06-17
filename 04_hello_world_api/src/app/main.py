from fastapi import FastAPI, HTTPException

# create FastAPI application
app = FastAPI()


# root route, which is shown if the API is called
@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


# pretty simple route, which calculates the square root of an input number that is sent by HTTP GET parameter
@app.get(
    "/sqrt/{number}",
    summary="Get the square root of a number",
    description="Type a number which is greater than 0",
)
async def sqrt(number: float) -> dict:
    if number < 0.0:
        raise HTTPException(status_code=400, detail="Wrong input")
    res = number**0.5
    return {"result": res}
