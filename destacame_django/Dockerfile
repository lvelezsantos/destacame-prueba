FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Configure server packages
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y python3 python3-dev postgresql-server-dev-all \
                       python3-pip git binutils libproj-dev

RUN apt-get install -y locales
RUN apt-get install -y tzdata

# Fixing Locales
RUN locale-gen en_US.UTF-8
RUN echo 'LC_ALL=en_US.UTF8' >> '/etc/default/locale'
RUN echo 'LANG=en_US.UTF8' >> '/etc/default/locale'
RUN echo 'LC_CTYPE=en_US.UTF8' >> '/etc/default/locale'
RUN echo 'LC_COLLATE=en_US.UTF8' >> '/etc/default/locale'
RUN chmod 0755 /etc/default/locale
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8

## USE Python3.6 AND PIP3 BY DEFAULT
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# Configure tzdata
RUN echo "Etc/UTC" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

WORKDIR /code

COPY requirements.txt requirements.txt
RUN  pip3 install -r /code/requirements.txt

ARG CODE_VERSION=1
COPY . .
# Installing requirements
COPY destacame/local_settings.docker.py /code/destacame/local_settings.py

# install requirements




## DO NOT RUN CELERY / UWSGI AS ROOT
RUN groupadd -g 1000 -r django && useradd -r -u 1000 -g django django
USER django
