# Hello world in FastAPI
This example is built on FastAPI, which is a web framework for building APIs with Python. It delves into REST API
programming.

If you're new to FastAPI and/or Python, this is the first example you should take a look at.
First, call the Python file `src/app/main.py`. The whole FastAPI server is created there.


## Architecture

One container is specified in the `docker-compose.yml` in this directory:

- simple-api (FastAPI/Python)


## Use case

Interact with FastAPI via SwaggerUI, which is available at `http://localhost:8000/docs`. FastAPI builds this interface
automatically, and it contains all routes of your API. The UI is for dev-purposes, so you can test all routes there.


## Setup

The containers are created automatically when building all Docker containers. Run the following command in a terminal
in this directory to build them:

~~~~
docker-compose up -d --build
~~~~

This builds all Docker containers specified in the `docker-compose.yml` file.
The associated Dockerfile is located in the `./src` folder of this directory.
