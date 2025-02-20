#!/bin/sh
echo Starting migrations
python manage.py makemigrations
echo Migrating
python manage.py migrate app
echo Running
exec gunicorn config.asgi:application --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker