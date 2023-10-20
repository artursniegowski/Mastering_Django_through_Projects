FROM python:3.11-alpine3.18
LABEL maintainer="artursniegowski"
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /temp/requirements.txt
COPY ./requirements.dev.txt /temp/requirements.dev.txt
COPY ./library_project /library_project
# added also docker ignore but technically not need
# as we specify precisly what we want to copy and nothing else

WORKDIR /library_project
EXPOSE 8000

ARG DEV=false

# adding dep to run psycopg: postgresql-libs postgresql-dev gcc musl-dev
RUN apk add --update --no-cache postgresql-libs postgresql-dev musl-dev && \
    apk add --update --no-cache --virtual .temp-build-deps \
        gcc && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /temp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /temp/requirements.dev.txt ; \
    fi && \
    rm -rf /temp && \
    # Remove the temporary build dependencies
    apk del .temp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol


ENV PATH="/py/bin:$PATH"

USER django-user