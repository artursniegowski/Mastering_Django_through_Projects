FROM python:3.12-alpine
LABEL maintainer="artursniegowski"

ENV PYTHONDONTWRITEBYTECODE 1 

ENV PYTHONUNBUFFERED 1

COPY ./requirements /temp/requirements/
COPY ./standalone_app /standalone_app
COPY ./docker/scripts/celery/start.sh /scripts/celery-start.sh

WORKDIR /standalone_app

RUN apk update --no-cache && \
    apk upgrade --no-cache && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /temp/requirements/base.txt && \
    # cleaning
    rm -rf /temp && \
    adduser \
        --disabled-password \
        --no-create-home \
        celery-user && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER celery-user

CMD ["celery-start.sh"]