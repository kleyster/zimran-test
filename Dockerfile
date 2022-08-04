FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app/

COPY . .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -Ur requirements.txt