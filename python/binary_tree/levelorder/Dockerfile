
FROM python:3.8-slim-buster

WORKDIR /levelorder

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "tests.py"]
