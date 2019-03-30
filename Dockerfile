FROM python:3.6

RUN apt-get update
RUN apt-get -y install jq
WORKDIR /app
COPY ./ /app

