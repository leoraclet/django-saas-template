#!/bin/sh

###############################################################################
# WAIT FOR POSTGRESQL TO BE ONLINE
###############################################################################

echo "Waiting for postgres..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

###############################################################################
###############################################################################

# python manage.py collectstatic --no-input --clear
# python manage.py flush --no-input
# python manage.py migrate

exec "$@"
