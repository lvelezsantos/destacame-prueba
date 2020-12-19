#!/bin/sh

docker-compose build
docker-compose up -d
docker-compose exec api bash -c "python manage.py migrate"
docker-compose exec api bash -c "python manage.py loaddatad initial_data.json"