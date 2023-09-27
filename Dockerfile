FROM python:3.10.12

COPY requirements.txt /temp/requirements.txt
COPY locallibrary /locallibrary

WORKDIR /locallibrary

EXPOSE 8000

RUN pip install -r /temp/requirements.txt