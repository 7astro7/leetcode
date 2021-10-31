
FROM python:3.8-slim-buster

WORKDIR /check_if_sentence_is_pangram

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
