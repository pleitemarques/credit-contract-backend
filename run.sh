#!/bin/sh
poetry run ./manage.py makemigrations
poetry run ./manage.py migrate
poetry run ./manage.py runserver 8001