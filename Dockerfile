FROM python:3.11-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./proj/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

