FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY /Pipfile.lock /Pipfile /app/

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

COPY /.env /app
COPY /server/users /app
