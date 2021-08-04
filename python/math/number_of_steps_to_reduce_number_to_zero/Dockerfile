
FROM python:3.8-slim-buster

WORKDIR /number_of_steps_to_reduce_a_number_to_zero

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
