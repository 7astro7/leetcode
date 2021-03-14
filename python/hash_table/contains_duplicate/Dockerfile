
FROM python:3.8-slim-buster

WORKDIR /contains_duplicate

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
