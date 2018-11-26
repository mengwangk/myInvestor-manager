FROM python:latest

LABEL maintainer "Koh Meng Wang <mengwangk@gmail.com>"

ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV=development

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system

RUN mkdir /app
COPY . /app
WORKDIR /app

EXPOSE 5000

# RUN mkdir /code
# WORKDIR /code
# ADD requirements.txt /code/
# RUN pip install --no-cache-dir -r requirements.txt
# ADD . /code
# EXPOSE 5000
