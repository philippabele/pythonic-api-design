FROM python:3.10

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./01_simple_crud_sql/src/ /code/

WORKDIR /code/src
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
