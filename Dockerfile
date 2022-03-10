FROM python:3.8.6

RUN apt-get update \
 && apt-get install -y wget

RUN mkdir /usr/src/app
COPY requirements.txt /usr/src/app/

RUN cd /usr/src/app \
 && pip install --upgrade pip \
 && pip install -r requirements.txt
RUN pip install wandb

WORKDIR /usr/src/app

COPY main.py .

EXPOSE 8080

ENTRYPOINT uvicorn main:app --port 8080 --host 0.0.0.0

