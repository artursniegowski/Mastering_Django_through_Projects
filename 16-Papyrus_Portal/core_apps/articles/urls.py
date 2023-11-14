"""
urls mapping for the Article.
"""
from django.urls import path

from .views import (
    ArticleListCreateView,
    ArticleRetrieveUpdateDestroyView,
    ClapArticleView,
)

app_name = "articles"

urlpatterns = [
    path("", ArticleListCreateView.as_view(), name="articles-list-create"),
    path(
        "<uuid:id>/",
        ArticleRetrieveUpdateDestroyView.as_view(),
        name="article-retrieve-update-destroy",
    ),
    path("<uuid:article_id>/clap/", ClapArticleView.as_view(), name="clap-article"),
]
