#!/bin/sh

python manage.py migrate --noinput

exec gunicorn config.wsgi:application --bind 0.0.0.0:80 --log-level info --forwarded-allow-ips "*"