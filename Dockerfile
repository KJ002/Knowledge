FROM python:3.9-slim

RUN mkdir /app

ADD . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "bot"]