"""
urls mapping for the Rating.
"""
from django.urls import path

from .views import RatingCreateView

app_name = "ratings"

urlpatterns = [
    path(
        "rate_article/<uuid:article_id>/",
        RatingCreateView.as_view(),
        name="rating-create",
    ),
]
