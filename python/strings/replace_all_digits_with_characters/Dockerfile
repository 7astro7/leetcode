
FROM python:3.8-slim-buster

WORKDIR /replace_all_digits_with_characters

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
