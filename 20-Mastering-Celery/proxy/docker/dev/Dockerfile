FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./docker/dev/default.conf.template /etc/nginx/templates/default.conf.template

ENV LISTEN_PORT=80
ENV DOMAIN_NAME=localhost
ENV BACKEND_SERVICE=backend
ENV BACKEND_PORT=8000

EXPOSE 80

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf

VOLUME /vol/static

USER nginx