FROM python:3.7.7-slim
EXPOSE 9080

ENV GROUP_NUMBER=22

RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
RUN apt-get update
RUN apt-get install -y python3-pip

WORKDIR practica_creativa2/bookinfo/src/productpage

RUN pip3 install -r requirements.txt
RUN pip3 install urllib3

CMD python3 productpage.py 9080
