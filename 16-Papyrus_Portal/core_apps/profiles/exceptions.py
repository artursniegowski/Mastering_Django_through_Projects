"""
Custom profile exceptiions
"""
from rest_framework.exceptions import APIException


class CantFollowYourself(APIException):
    """User can follow its own profile - 403 forbidden"""

    status_code = 403
    default_detail = "You can't follow yurself."
    default_code = "forbidden"
