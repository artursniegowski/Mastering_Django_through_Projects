"""
custom pagination for the Profile
"""
from rest_framework.pagination import PageNumberPagination


class ProfilePagination(PageNumberPagination):
    """custom pagination for the profile model"""

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 20
