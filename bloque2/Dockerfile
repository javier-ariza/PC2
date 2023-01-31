FROM ubuntu:18.04

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
RUN sed -i "/REVIEWS_HOSTNAME/i\ \ngroupNumber = int(os.environ.get('GROUP_NUMBER', '0')) \n" productpage_monolith.py
RUN sed -i "/front/a\    group = groupNumber/1" productpage_monolith.py
RUN sed -i "/productpage.html/a\ \tgroup=group," productpage_monolith.py
RUN sed -i '/Simple Bookstore App/c {% block title %}Grupo {{group}}{% endblock %}' templates/productpage.html

CMD python3 productpage_monolith.py 9080
