FROM python:3.10

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD takes a list of strings, each of these strings is what you would type in the command line separated by spaces.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]