"""
Views for the Rating model
"""
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from core_apps.articles.models import Article
from core_apps.ratings.exceptions import YouHaveAlreadyRated

from .models import Rating
from .serializers import RatingSerializer


class RatingCreateView(CreateAPIView):
    """Rating create view"""

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """overiding the perform create method because we want to set our
        author field to the request user"""
        article_id = self.kwargs.get("article_id")
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
            except Article.DoesNotExist:
                raise ValidationError("Invalid article_id provided.")
        else:
            raise ValidationError("article_id is required.")

        try:
            serializer.save(user=self.request.user, article=article)
        except IntegrityError:
            raise YouHaveAlreadyRated
