#!/bin/sh
python manage.py collectstatic --no-input

gunicorn bsb_lottery.wsgi:application --bind 0.0.0.0:8002 --workers 4