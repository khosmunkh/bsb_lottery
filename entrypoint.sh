#!/bin/sh
python manage.py collectstatic --no-input

gunicorn bsb_margaash.wsgi:application --bind 0.0.0.0:8001 --workers 4