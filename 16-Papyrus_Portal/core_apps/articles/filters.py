"""
Custom filters for Articles
"""
from django_filters import CharFilter, DateFromToRangeFilter, FilterSet

from core_apps.articles.models import Article


class ArticleFilter(FilterSet):
    """custom filter for Article"""

    author = CharFilter(field_name="author__first_name", lookup_expr="icontains")
    title = CharFilter(field_name="title", lookup_expr="icontains")
    tags = CharFilter(field_name="tags__name", lookup_expr="iexact")
    created_at = DateFromToRangeFilter(field_name="created_at")
    updated_at = DateFromToRangeFilter(field_name="updated_at")

    class Meta:
        model = Article
        fields = ["author", "title", "tags", "created_at", "updated_at"]
