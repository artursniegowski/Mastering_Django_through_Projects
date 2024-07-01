#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

exec celery -A app.celery worker --hostname=celeryWorker1@%h -l INFO -Q tasks,dead_letter -E -B