FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/requirements.txt
COPY entrypoint.sh /tmp/entrypoint.sh

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

RUN chmod 777 /tmp/entrypoint.sh

COPY app /app

WORKDIR /app

EXPOSE 8000