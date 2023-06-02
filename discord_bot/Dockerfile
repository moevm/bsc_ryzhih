FROM python:3.10

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install inetutils-ping

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]