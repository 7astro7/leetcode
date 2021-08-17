
FROM python:3.8-slim-buster

WORKDIR /maximum_product_of_two_elements_in_an_array

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
