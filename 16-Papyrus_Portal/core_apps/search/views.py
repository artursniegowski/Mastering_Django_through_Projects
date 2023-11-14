"""
Views for elasticsearch
"""
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework.permissions import AllowAny

from .documents import ArticleDocument
from .serializers import ArticleElasticSearchSerializer


class ArticleElasticSearchView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleElasticSearchSerializer
    lookup_field = "id"  # set to use default primary ley field lookup
    # bc we want to allow anyone weater logged in or not to be able to search
    permission_classes = [AllowAny]
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # by what we ant to search our articles
    search_fields = (
        "title",
        "description",
        "body",
        "author_first_name",
        "author_last_name",
        "tags",
    )

    filter_fields = {
        # slog.raw => to perform exact matching
        "slug": "slug.raw",
        "tags": "tags",
        "created_at": "created_at",
    }

    # dictionary used for ordering
    # the key are going to be the field name
    # and the alues are going to be field paths in the ElasticSearch
    ordering_fields = {"created_at": "created_at"}
    ordering = ("-created_at",)
