### docker commands - START ###
build:
	docker-compose build

build-no-cache:
	docker-compose build --no-cache

up:
	docker-compose up -d

up-attached: 
	docker-compose up

down:
	docker-compose down

down-remove-volumes:
	docker-compose down -v

show-logs-all:
	docker-compose logs

# show-logs svc=db
show-logs:
	docker-compose logs	$(svc)

### docker commands - END ###

### linting / test coverege / formating commands - START ###
flake8:
	docker-compose run --rm backend sh -c "flake8"

flake8-exec:
	docker-compose exec backend sh -c "flake8 ."

black-check:
	docker-compose run --rm backend sh -c "black --check --exclude=migrations ."

black-check-exec:
	docker-compose exec backend sh -c "black --check --exclude=migrations ."

black-diff:
	docker-compose run --rm backend sh -c "black --diff --exclude=migrations ."

black-diff-exec:
	docker-compose exec backend sh -c "black --diff --exclude=migrations ."

black:
	docker-compose run --rm backend sh -c "black --exclude=migrations ."

black-exec:
	docker-compose exec backend sh -c "black --exclude=migrations ."

isort-check:
	docker-compose run --rm backend sh -c "isort . --check-only --skip ENV --skip migrations"

isort-check-exec:
	docker-compose exec backend sh -c "isort . --check-only --skip ENV --skip migrations"

isort-diff:
	docker-compose run --rm backend sh -c "isort . --diff --skip ENV --skip migrations"

isort-diff-exec:
	docker-compose exec backend sh -c "isort . --diff --skip ENV --skip migrations"

isort:
	docker-compose run --rm backend sh -c "isort . --skip ENV --skip migrations"

isort-exec:
	docker-compose exec backend sh -c "isort . --skip ENV --skip migrations"

coverage-run-report:
	docker-compose run --rm backend sh -c "coverage run manage.py test && coverage report"

coverage-run-report-exec:
	docker-compose exec backend sh -c "coverage run manage.py test && coverage report"

coverage-run-html:
	docker-compose run --rm backend sh -c "coverage run manage.py test && coverage html"

coverage-run-html-exec:
	docker-compose exec backend sh -c "coverage run manage.py test && coverage html"

# runnign combined - black - isort - flake8
format:
	docker-compose run --rm backend sh -c "black --exclude=migrations . && isort . --skip ENV --skip migrations && flake8"
### linting / test coverege / formating commands - END ###

### django commands - START ###
start-project:
	docker-compose run --rm backend sh -c "django-admin startproject app ." 

start-project-exec:
	docker-compose exec backend sh -c "django-admin startproject app ."

# make start-app app=app_name
start-app:
	docker-compose run --rm backend sh -c "python manage.py startapp $(app)"

start-app-exec:
	docker-compose exec backend sh -c "python manage.py startapp $(app)"

makemigrations:
	docker-compose run --rm backend sh -c "python manage.py makemigrations"

makemigrations-exec:
	docker-compose exec backend sh -c "python manage.py makemigrations"

migrate:
	docker-compose run --rm backend sh -c "python manage.py migrate"

migrate-exec:
	docker-compose exec backend sh -c "python manage.py migrate"

collectstatic:
	docker-compose run --rm backend sh -c "python manage.py collectstatict --no-input --clear"

collectstatic-exec:
	docker-compose exec backend sh -c "python manage.py collectstatict --no-input --clear"

superuser: 
	docker-compose run --rm backend sh -c "python manage.py createsuperuser"

superuser-exec: 
	docker-compose exec backend sh -c "python manage.py createsuperuser"

test:
	docker-compose run --rm backend sh -c "python manage.py test"

test-exec:
	docker-compose exec backend sh -c "python manage.py test"

test-spec:
	docker-compose run --rm backend sh -c "python manage.py test $(test)"

test-spec-exec:
	docker-compose exec backend sh -c "python manage.py test $(test)"

test-parallel:
	docker-compose run --rm backend sh -c "python manage.py test --parallel auto"

test-parallel-exec:
	docker-compose exec backend sh -c "python manage.py test --parallel auto"

django-checklist-deployment:
	docker-compose run --rm backend sh -c "python manage.py check --deploy"

django-checklist-deployment-exec:
	docker-compose exec backend sh -c "python manage.py check --deploy"
### django commands - END ###
