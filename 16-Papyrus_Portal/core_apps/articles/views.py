"""
Views for the Article model
"""
import logging

from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .filters import ArticleFilter
from .models import Article, ArticleView, Clap
from .pagination import ArticlePagination
from .permissions import IsOwnerOrReadOnly
from .renderers import ArticleJSONRenderer, ArticlesJSONRenderer
from .serializers import ArticleSerializer, ClapSerializer

User = get_user_model()
logger = logging.getLogger(__name__)


class ArticleListCreateView(ListCreateAPIView):
    """Article view"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ArticlePagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ArticleFilter
    ordering_fields = ["created_at", "updated_at"]
    renderer_classes = [ArticlesJSONRenderer]

    def perform_create(self, serializer):
        """overiging the perform create method because we want to set our
        author field to the request user"""
        serializer.save(author=self.request.user)
        logger.info(
            f"article {serializer.data.get('title')} created by {self.request.user.first_name}"
        )


class ArticleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """udapting an article"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "id"
    renderer_classes = [ArticleJSONRenderer]
    parser_classes = [MultiPartParser, FormParser]

    def perform_update(self, serializer):
        """overiging the perform update method because we want to set our
        author field to the request user"""
        instance = serializer.save(author=self.request.user)
        # when we update an article we check if the banner image is in the request
        # Files, and if so we going to delete the old image file if it exists
        # and is not the default image
        if "banner_image" in self.request.FILES:
            if (
                instance.banner_image
                and instance.banner_image.name != "/profile_default.png"
            ):
                # if it exists then we can delete it
                default_storage.delete(instance.banner_image.path)
            instance.banner_image = self.request.FILES["banner_image"]
            instance.save()

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        # incrementing the article views by first getting the viewers IP
        # from the requests meta attribute
        viewer_ip = request.META.get("REMOTE_ADDR", None)

        ArticleView.record_view(
            article=instance, user=request.user, viewer_ip=viewer_ip
        )

        return Response(serializer.data)


class ClapArticleView(CreateAPIView, DestroyAPIView):
    """view for the Clap model"""

    queryset = Clap.objects.all()
    serializer_class = ClapSerializer

    def create(self, request, *args, **kwargs):
        """overiding the creaet method - checking if the article was alredy
        clapped by the user"""
        user = request.user
        article_id = kwargs.get("article_id")
        article = get_object_or_404(Article, id=article_id)

        if Clap.objects.filter(user=user, article=article).exists():
            return Response(
                {"detail": "You have already clapped on this article."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        clap = Clap.objects.create(user=user, article=article)  # noqa
        return Response(
            {"detail": "Clap added to article."}, status=status.HTTP_201_CREATED
        )

    def delete(self, request, *args, **kwargs):
        """overiding the delete method - checking if the article was clapped
        by the given user"""
        user = request.user
        article_id = kwargs.get("article_id")
        article = get_object_or_404(Article, id=article_id)

        clap = get_object_or_404(Clap, user=user, article=article)
        clap.delete()
        return Response(
            {"detail": "Clap removed from article."}, status=status.HTTP_204_NO_CONTENT
        )
