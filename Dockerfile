FROM python:3.6.6-alpine3.7
ENV LANG C.UTF-8

# for mypy ====
RUN apk add gcc
RUN apk add musl-dev
# ====

RUN apk add make
RUN pip install pipenv
RUN mkdir /app

COPY Pipfile /app/Pipfile
WORKDIR /app
RUN pipenv install --dev
