FROM python:3.5

MAINTAINER Evgeny Shakhmaev

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./ .