FROM ubuntu:17.10
LABEL maintainer="yamila.ms@gmail.com"

WORKDIR /

# Install dependencies
RUN apt-get update
RUN apt-get install -y -qq curl python3-pip vim
RUN pip3 install virtualenv

# Install requirements
RUN virtualenv -p python3 myvenv
COPY requirements.txt /routes_api/
RUN /myvenv/bin/easy_install --upgrade requests
RUN /myvenv/bin/pip install -r /routes_api/requirements.txt

# Setup the application
COPY . /routes_api

WORKDIR /routes_api
