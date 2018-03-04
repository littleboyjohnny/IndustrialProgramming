#!/usr/bin/env bash

sudo docker build . -t django
sudo docker run -d -p 8000:8000 --name=dj --net=host django python todo/manage.py runserver
sudo docker exec -d dj python todo/manage.py makemigrations
sudo docker exec -d dj python todo/manage.py migrate



