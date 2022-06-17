# Simple CRUD SQL

This example is built on FastAPI, which is a web framework for building APIs with Python. It delves into REST API
programming.
This section is about Python Types and Pydantic, which is very useful to define custom models.

Python is a dynamically typed language, so you never have to declare the data type for a variable. But in most cases,
this is very handy. The first benefit is that other programmers understand what types of data to expect. Second,
type hints are used by the Python Interpreter to check your code at runtime, which saves you from tedious debugging.
And last but not least it is super useful to use autocompletion in your IDE (Integrated development environment).

With Pydantic you can declare custom classes, which goes beyond simple types.

Take a look at these sites of FastAPI guide for further information:
- https://fastapi.tiangolo.com/features/#pydantic-features
- https://fastapi.tiangolo.com/python-types/?h=type+hint

## Architecture

One container is specified in the `docker-compose.yml` in this directory:

- pydantic-api (FastAPI/Python)


## Use case

A type hint in Python is defined as follows: `custom_name: str`. You can also assign a value to this variable: `custom_name: str = "Someone"`.
Wrapped in a FastAPI function type hints look like this: 
~~~
@app.post("/person")
async def person(name: str, lastname: str, age: int) -> dict:
    ...
~~~

And now use `Pydantic` to create your own model:
~~~
class Person(BaseModel):
    name: str
    lastname: str
    age: int
~~~

Interact with FastAPI via SwaggerUI, which is available at `http://localhost:8000/docs`. FastAPI builds this interface
automatically and contains all routes of your API. It is for dev-purposes, so you can test all routes there.
The defined classes/models are expandable and shown at the bottom of the page.

## Setup

The container is created automatically when building all Docker containers. Run the following command in a terminal 
in this directory to build it:

~~~~
docker-compose up -d --build
~~~~

This builds all Docker containers specified in the `docker-compose.yml` file.
The associated Dockerfile is located in the `./src` folder of this directory.
