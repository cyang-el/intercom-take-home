FROM python:3.6.6-alpine3.7
ENV LANG C.UTF-8

# for mypy ====
RUN apk add gcc
RUN apk add musl-dev
# ====

RUN apk add make
RUN pip install pipenv
RUN mkdir -p /pipeline/source

COPY Pipfile /pipeline/source/Pipfile
COPY Pipfile.lock /pipeline/source/Pipfile.lock
WORKDIR /pipeline/source
RUN pipenv install --dev
