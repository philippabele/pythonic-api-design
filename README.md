
<p align="center">

<a href="https://github.com/philippabele/pythonic-api-design/actions/workflows/pytest.yaml" target="_blank">
    <img src="https://github.com/philippabele/pythonic-api-design/workflows/Test/badge.svg" alt="Test">
</a>

<img src="https://img.shields.io/badge/Python-3.6%7C3.7%7C3.8%7C3.9-brightgreen" alt="Python">


</p>

# pythonic-api-design

## Docker:
First, please install Docker Desktop from this [LINK](https://docs.docker.com/desktop/#download-and-install).
### Build Docker Image with the following command:
`docker build -t pythonic-api-design .`

### Run it with:
`docker  run -d --name pythonic-api -p 80:80 pythonic-api-design`


## Run FastAPI from terminal:
`uvicorn app.main:app --port 80`
