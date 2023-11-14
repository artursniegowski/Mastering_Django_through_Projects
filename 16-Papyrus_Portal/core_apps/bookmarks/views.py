"""
Views for the Bookmark model
"""
from uuid import UUID

from django.db import IntegrityError
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from core_apps.articles.models import Article

from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkCreateView(CreateAPIView):
    """Bookmark create view"""

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
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
            raise ValidationError("You have already bookmarked this article.")


class BookmarkDestroyView(DestroyAPIView):
    """Bookmark destroy view"""

    queryset = Bookmark.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "article_id"

    def get_object(self):
        """gets the specific user instace that the user tries to delete"""
        user = self.request.user
        article_id = self.kwargs.get("article_id")

        try:
            # checking if the article_id is a valid UUID of verions four
            UUID(str(article_id), version=4)
        except ValueError:
            raise ValidationError("Invalid article_id provided.")

        try:
            bookmark = Bookmark.objects.get(user=user, article__id=article_id)
        except Bookmark.DoesNotExist:
            raise NotFound("Bookmark not found or it doesn't belong to you.")

        return bookmark

    def perform_destroy(self, instance):
        """overiding the delete perfom method"""
        user = self.request.user
        if instance.user != user:
            raise ValidationError("You cannot delete a bookmark that is not yours.")
        instance.delete()
