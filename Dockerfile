FROM python:3.6

RUN apt-get update
WORKDIR /app
COPY ./ /app

