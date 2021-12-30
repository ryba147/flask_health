# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /flask-health-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV SQLALCHEMY_DATABASE_URI "postgresql://taras_docker:taras_docker@db:5432/flask_health_docker_db"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
