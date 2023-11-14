"""
Serializer for the Search - elasticsearch
"""
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from core_apps.search.documents import ArticleDocument


class ArticleElasticSearchSerializer(DocumentSerializer):
    """elastic search serializer for the ArticleDocument"""

    class Meta:
        document = ArticleDocument
        fields = [
            "title",
            "author",
            "slug",
            "description",
            "body",
            "created_at",
        ]
