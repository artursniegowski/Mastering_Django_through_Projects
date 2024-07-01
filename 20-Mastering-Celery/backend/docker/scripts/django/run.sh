#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000
