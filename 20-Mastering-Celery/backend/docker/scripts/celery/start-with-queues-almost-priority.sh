#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

exec celery -A app.celery worker -l INFO -Q celery,celery:1,celery:2,celery:3