"""
urls mapping for the Response.
"""
from django.urls import path

from .views import ResponseListCreateView, ResponseUpdateDeleteView

app_name = "responses"

urlpatterns = [
    path(
        "article/<uuid:article_id>/",
        ResponseListCreateView.as_view(),
        name="article-responses",
    ),
    path("<uuid:id>/", ResponseUpdateDeleteView.as_view(), name="response-detail"),
]
