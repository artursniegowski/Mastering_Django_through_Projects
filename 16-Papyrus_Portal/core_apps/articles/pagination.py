"""
custom pagination for the Article
"""
from rest_framework.pagination import PageNumberPagination


class ArticlePagination(PageNumberPagination):
    """custom pagination for the Article model"""

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 30
