
FROM python:3.8-slim-buster

WORKDIR /relative_ranks

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
