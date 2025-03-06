FROM python:3.12.7-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libmagic1 libmagic-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./creds/creds.json /opt/creds.json
COPY . .