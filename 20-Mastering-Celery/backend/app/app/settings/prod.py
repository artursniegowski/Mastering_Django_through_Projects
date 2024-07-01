"""
Settings for production environment
"""

from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO: need to be defined!
# CORS HEADERS
# A list of origins that are authorized to make cross-site HTTP requests.
# so the orgins from nginx
# https://pypi.org/project/django-cors-headers/
# CORS_ALLOWED_ORIGINS = ["http://localhost", "http://localhost:8080"]
