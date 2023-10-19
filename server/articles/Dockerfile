FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /articles

COPY /Pipfile.lock /Pipfile /articles/

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

COPY /server/articles /articles
