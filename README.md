
![example branch parameter](https://github.com/philippabele/pythonic-api-design/actions/workflows/pytest.yaml/badge.svg)

# pythonic-api-design

## Docker:
First, please install Docker Desktop from this [LINK](https://docs.docker.com/desktop/#download-and-install).
### Build Docker Image with the following command:
`docker build -t pythonic-api-design .`

### Run it with:
`docker  run -d --name pythonic-api -p 80:80 pythonic-api-design`


## Run FastAPI from terminal:
`uvicorn app.main:app --port 80`