"""
urls mapping for the Bookmarks.
"""
from django.urls import path

from .views import BookmarkCreateView, BookmarkDestroyView

app_name = "bookmarks"

urlpatterns = [
    path(
        "bookmark_article/<uuid:article_id>/",
        BookmarkCreateView.as_view(),
        name="bookmark-article",
    ),
    path(
        "remove_bookmark/<uuid:article_id>/",
        BookmarkDestroyView.as_view(),
        name="remove-bookmark",
    ),
]
