"""
Serializer for the Responses model
"""
from rest_framework import serializers

from core_apps.responses.models import Response


class ResponseSerializer(serializers.ModelSerializer):
    """Model serializer for Responses"""

    article_title = serializers.CharField(source="article.title", read_only=True)
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)

    class Meta:
        model = Response
        fields = [
            "id",
            "article_title",
            "user_first_name",
            "parent_response",
            "content",
            "created_at",
        ]
