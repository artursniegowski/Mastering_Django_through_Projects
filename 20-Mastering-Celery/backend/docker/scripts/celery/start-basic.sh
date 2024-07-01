#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

exec celery -A app.celery worker -l INFO