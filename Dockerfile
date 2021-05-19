# syntax=docker/dockerfile:1
FROM python:3.8.3-alpine

RUN apk update \
 && apk add postgresql-dev gcc python3-dev musl-dev libc-dev
RUN apk add --no-cache linux-headers


# Set working directory
WORKDIR .
COPY ./requirements.txt /code/requirements.txt

#Gathering all the static file to the asset folder
COPY ./web-front/dist /code/static



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


