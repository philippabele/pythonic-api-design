# Async in FastAPI

This example is built on FastAPI, which is a web framework for building APIs with Python.
A major advantage of FastAPI is the ability to run concurrent code, so multiple tasks can run at the same time.
With async functions Python is able to run further commands, while a slow command is executed and wait for its 
completion. This is common for I/O tasks and reduces the wasted time when Python has to wait.

This example is based on `Christopher Samiullahs`
[guide](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-9-asynchronous-performance-basics/).
Check out his guide to learn more about async tasks and to get a deeper insight.

To understand the difference between parallelism and concurrency, check out the 
[FastAPI guide](https://fastapi.tiangolo.com/async/).


## Architecture

One container is specified in the `docker-compose.yml` in this directory:

- api-async (FastAPI/Python)


## Use case

Interact with FastAPI via SwaggerUI, which is available at `http://localhost:8000/docs`. FastAPI builds this interface
automatically and contains all routes of your API. It is for dev-purposes, so you can test all routes there.

There are two routes, one is built asynchronously and the other one synchronously. The asynchronous example is much 
faster. You can compare the process time by looking at the response headers:
![response_header.png](response_header.png "Response headers")

## Setup

The container is created automatically by running the following command in a terminal 
in this directory:

~~~~
docker-compose up -d --build
~~~~

This builds the Docker container specified in the `docker-compose.yml` file.
The associated Dockerfile is located in the `./src` folder of this directory.
