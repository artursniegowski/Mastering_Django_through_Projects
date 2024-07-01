"""
Settings for local - development environment
"""

import socket

from .base import *  # noqa

# Application definition

INSTALLED_APPS += [
    # third party apps
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    "debug_toolbar",
]

# configuration for the debug toolbar - START #
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
# Configure Internal IPs
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configure-internal-ips
if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",  # localhost
        "10.0.2.2",  # most likely used by virtual machines
    ]
    # Adding IP addresses dynamically based on the local machine's hostname
    # https://github.com/cookiecutter/cookiecutter-django/blob/df529fc9e4d16bfe16f76e0e620c2f543f740ba3/%7B%7Bcookiecutter.project_slug%7D%7D/config/settings/local.py#L74  # noqa
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
    # adding dynamically ip for nginx - so the tolbar be also visible when served with the proxy
    # https://stackoverflow.com/questions/64284647/get-nginx-ip-address-in-docker-in-django-settings-py-for-django-debug-toolbar
    try:
        _, _, nginx_ips = socket.gethostbyname_ex("nginx")
        INTERNAL_IPS.extend(nginx_ips)
    except socket.gaierror:
        # the nginx service didnt start yet?
        pass
# configuration for the debug toolbar - END #
