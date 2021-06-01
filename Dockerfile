FROM python:3

RUN apt-get update \
 && apt-get install -y wget

RUN mkdir /usr/src/app
COPY requirements.txt /usr/src/app/

RUN cd /usr/src/app \
 && pip install --upgrade pip \
 && pip install -r requirements.txt

WORKDIR /usr/src/app

RUN wget https://repository.clarin.is/repository/xmlui/bitstream/handle/20.500.12537/98/tagger-v2.0.0.pt
#COPY tagger-v2.0.0.pt .
COPY ./example.txt .
COPY main.py .

EXPOSE 8080

ENTRYPOINT uvicorn main:app --port 8080 --host 0.0.0.0

