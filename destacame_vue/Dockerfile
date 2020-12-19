FROM node:14.15.3-buster

WORKDIR /code
ARG PACKAGE_VER=1
COPY package*.json ./
RUN npm install

ARG FRONT_VER=1
COPY . .

COPY src/config.docker.js /code/src/config.js

