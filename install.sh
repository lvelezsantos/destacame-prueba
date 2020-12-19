#!/bin/sh

docker-compose build
docker-compose up -d
docker-compose exec api bash -c "python manage.py migrate"
docker-compose exec api bash -c "python manage.py loaddata initial_data.json"
echo "\n\n\n\n\n\n  ***** Colocal esta url en tu navegador http://localhost:9030/ **** \n\n\n\n\n\n "