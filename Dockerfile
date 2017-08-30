FROM python:3.6-slim
LABEL maintainer="yamila.ms@gmail.com"

WORKDIR /

# Install dependencies
RUN apt-get update
RUN apt-get install -y -qq curl vim

# Install requirements
COPY requirements.txt /routes_api/
RUN pip install -r /routes_api/requirements.txt

# Setup the application
COPY . /routes_api

WORKDIR /routes_api
