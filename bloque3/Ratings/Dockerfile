FROM node:12.18.1-slim

COPY package.json /opt/microservices/
COPY ratings.js /opt/microservices/

RUN apt-get update


ENV SERVICE_VERSION v3

RUN npm install

EXPOSE 9080

CMD node ratings.js 9080
