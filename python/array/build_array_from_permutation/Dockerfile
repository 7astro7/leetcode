
FROM python:3.8-slim-buster

WORKDIR /build_array_from_permutation

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
