# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv
