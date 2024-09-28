FROM python:3.10-buster

LABEL description="Remote Container Test"
LABEL version="1.0"

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH "/"
WORKDIR /app
