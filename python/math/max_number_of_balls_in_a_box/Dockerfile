
FROM python:3.8-slim-buster

WORKDIR /max_numbers_of_balls_in_a_box

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
