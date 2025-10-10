#!/bin/bash

set -euo pipefail

python manage.py migrate --noinput

python manage.py collectstatic --noinput

exec gunicorn src.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --access-logfile - \
    --error-logfile -
