
FROM python:3.8-slim-buster

WORKDIR /power-of-2

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
