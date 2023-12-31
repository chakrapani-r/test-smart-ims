FROM python:3.11.5
WORKDIR /code
COPY ./app/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "--app-dir=app",  "main:app", "--host", "0.0.0.0", "--port", "80"]

