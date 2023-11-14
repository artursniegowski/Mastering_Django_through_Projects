"""
Custom Rating exceptiions
"""
from rest_framework.exceptions import APIException


class YouHaveAlreadyRated(APIException):
    """Ua user cant rate twice an article - 400 bad request"""

    status_code = 400
    default_detail = "have already rated this article."
    default_code = "bad_request"
