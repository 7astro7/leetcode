
FROM python:3.8-slim-buster

WORKDIR /delete-node-linked-list

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
