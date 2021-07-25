
FROM python:3.8-slim-buster

WORKDIR /minimum_depth_binary_tree

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
