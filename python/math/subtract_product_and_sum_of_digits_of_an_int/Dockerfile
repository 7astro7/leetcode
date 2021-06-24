
FROM python:3.8-slim-buster

WORKDIR /subtract-prod-sum

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
