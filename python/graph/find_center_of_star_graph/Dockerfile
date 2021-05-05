
FROM python:3.8-slim-buster

WORKDIR /find-center-of-star-graph

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
