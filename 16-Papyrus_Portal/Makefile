build:
	docker-compose -f local.yml up --build -d --remove-orphans

up:
	docker-compose -f local.yml up -d

up-continuosly:
	docker-compose -f local.yml up

down:
	docker-compose -f local.yml down

show-logs:
	docker-compose -f local.yml logs

show-logs-api:
	docker-compose -f local.yml logs api

show-logs-api-continuosly:
	docker-compose -f local.yml logs -f api

makemigrations:
	docker-compose -f local.yml run --rm api python manage.py makemigrations

migrate:
	docker-compose -f local.yml run --rm api python manage.py migrate

collectstatic:
	docker-compose -f local.yml run --rm api python manage.py collectstatict --no-input --clear

superuser: 
	docker-compose -f local.yml run --rm api python manage.py createsuperuser

down-remove-volumes:
	docker-compose -f local.yml down -v

volume-inspect:
	docker volume inspect src_local_postgres_data

inspect-papyrus-portal-db:
	docker-compose -f local.yml exec postgres psql --username=testuser --dbname=papyrus-portal-data

flake8:
	docker-compose -f local.yml exec api flake8 .

black-check:
	docker-compose -f local.yml exec api black --check --exclude=migrations .

black-diff:
	docker-compose -f local.yml exec api black --diff --exclude=migrations .

black:
	docker-compose -f local.yml exec api black --exclude=migrations .

isort-check:
	docker-compose -f local.yml exec api isort . --check-only --skip venv --skip migrations

isort-diff:
	docker-compose -f local.yml exec api isort . --diff --skip venv --skip migrations

isort:
	docker-compose -f local.yml exec api isort . --skip venv --skip migrations

elasticsearch-create-index:
	docker-compose -f local.yml exec api python manage.py search_index --create

elasticsearch-populate:
	docker-compose -f local.yml exec api python manage.py search_index --populate

elasticsearch-rebuild:
	docker-compose -f local.yml exec api python manage.py search_index --rebuild

coverage-run:
	docker-compose -f local.yml run --rm api pytest -p no:warnings --cov=. -v

coverage-run-html:
	docker-compose -f local.yml run --rm api pytest -p no:warnings --cov=. --cov-report html

pytest-run-tests:
	docker-compose -f local.yml run --rm api pytest

django-checklist-deployment:
	docker-compose -f local.yml run --rm api python manage.py check --deploy
