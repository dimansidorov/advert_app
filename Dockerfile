FROM python:3.11-alpine3.18

RUN apk update \
    && apk add postgresql-client build-base postgresql-dev
RUN pip install --upgrade pip

COPY requirements.txt /temp/requirements.txt
COPY src /src

WORKDIR /src

EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password advert-user
USER advert-user

