# Simple CRUD SQL

This example is built on FastAPI, which is a web framework for building APIs with Python. It delves into REST API
programming.
The API stores data in PostgreSQL, a SQL database.

## Architecture

Two containers are specified in the `docker-compose.yml` in this directory:

- web (FastAPI/Python)
- db (Postgres)

API calls are received and executed by FastAPI. The data is stored in a PostgreSQL database. The credentials are
specified in environment variables in the `docker-compose.yml` below the service `db`.

## Use case

Interact with FastAPI via SwaggerUI, which is available at `http://localhost:8002/docs`. FastAPI builds this interface
automatically
and contains all routes of your API. It is for dev-purposes, so you can test all routes there.

Your data is stored and collected from PostgreSQL and you are able to run CRUD statements for tables (Create, Read,
Update, Delete).

## Setup

The containers are created automatically when building all Docker containers. Run the following command in a terminal 
in this directory to build them:

~~~~
docker-compose up -d --build
~~~~

This builds all Docker containers specified in the `docker-compose.yml` file.
The associated Dockerfile is located in the `./src` folder of this directory.