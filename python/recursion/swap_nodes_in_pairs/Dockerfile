
FROM python:3.8-slim-buster

WORKDIR /swap-nodes-in-pairs

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
