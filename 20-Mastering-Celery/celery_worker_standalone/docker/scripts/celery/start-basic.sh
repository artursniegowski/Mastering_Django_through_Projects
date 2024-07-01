#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

exec celery -A celery_tasks worker -l INFO