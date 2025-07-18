#!/bin/sh

# python manage.py collectstatic --no-input --clear
# python manage.py flush --no-input
# python manage.py migrate

# Create default super user
python manage.py createsuperuser --noinput

exec "$@"
