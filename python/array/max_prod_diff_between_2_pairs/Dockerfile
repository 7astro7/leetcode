
FROM python:3.8-slim-buster

WORKDIR /max_prod_diff_between_2_pairs

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
