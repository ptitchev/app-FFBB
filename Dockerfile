FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM jboss/keycloak

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app/app