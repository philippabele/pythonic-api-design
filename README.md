# Pythonic API design
[![Test status](https://github.com/philippabele/pythonic-api-design/workflows/Test/badge.svg)][test]
![Version badges](https://img.shields.io/badge/Python-3.6%7C3.7%7C3.8%7C3.9-brightgreen)

This project is a resource for future Python developers to help them get started in API programming.

[test]:https://github.com/philippabele/pythonic-api-design/actions/workflows/pytest.yaml

## Setup
First, please install Docker Desktop from this [LINK](https://docs.docker.com/desktop/#download-and-install). The 
installation depends on your OS.\
This introduction to API programming in python is split into seperated examples. Each is located in a subdirectory.
Navigate to an example, for example the first one by opening a terminal and running the following command:
~~~~
cd .\01_simple_crud_sql\ 
~~~~

Now you're in the subdirectory and can build all Docker containers of the specific example by running:
~~~~
docker-compose up -d --build
~~~~

<br>
There are detailed guides for each example. These are Markdown .md files and can be found in each sub-folder.
They are also linked below. 

## Documentation

- [Hello world FastAPI][]
- [Async API][]
- [Pydantic models][]
- [Simple CRUD SQL][]
- [Grafana][]
- [Elasticsearch][]


[Hello world FastAPI]: https://github.com/philippabele/pythonic-api-design/blob/development/04_hello_world_api/04_hello_fastapi.MD
[Async API]: https://github.com/philippabele/pythonic-api-design/blob/development/05_async_fastapi/05_async_fastapi.MD
[Simple CRUD SQL]: https://github.com/philippabele/pythonic-api-design/blob/development/01_simple_crud_sql/crud-sql.MD
[Grafana]: https://github.com/philippabele/pythonic-api-design/blob/development/03_grafana_monitoring/monitoring.MD
[Elasticsearch]: https://github.com/philippabele/pythonic-api-design/blob/development/02_simple_elastic_logging/elastic.MD
[Pydantic models]: https://github.com/philippabele/pythonic-api-design/blob/development/06_pydantic_modelling_fastapi/06_pydantic-api.MD
