FROM python:3.10

WORKDIR /root/MAIN

COPY .. 

RUN apt-get update && apt-get install ffmpeg -y
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -U -r requirements.txt


CMD ["python3", "-m", "MAIN"]
