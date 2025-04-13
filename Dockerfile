FROM python:3.10

WORKDIR /root/MAIN

COPY .. 

RUN pip3 install -upgrade pip supertools
RUN pip3 install -r requirements.txt


