#!/bin/bash
set -e

echo "DB_SERVICE=$DB_SERVICE"

if [ "$DB_SERVICE" = "RDS" ]; then
  echo " Running migrations for RDS..."
  python manage.py makemigrations
  python manage.py migrate
else
  echo " Skipping migration, DB_SERVICE=$DB_SERVICE"
fi

exec "$@"