#!/bin/bash

pip install -e /opt/app/microservice

mkdir -p /log

cd /opt/app/microservice

mkdir upload

gunicorn --timeout 120 --bind 0.0.0.0:8085 --config /opt/app/microservice/properties/config.ini wsgi:application

