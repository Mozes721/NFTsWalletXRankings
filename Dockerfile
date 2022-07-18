FROM python:3.9

RUN apt update && apt install --yes curl gcc

WORKDIR /src

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .