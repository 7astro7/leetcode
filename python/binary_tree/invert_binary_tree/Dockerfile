
FROM python:3.8-slim-buster

WORKDIR /invert_binary_tree

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
