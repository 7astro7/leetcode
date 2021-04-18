
FROM python:3.8-slim-buster

WORKDIR /symmetric_tree

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
