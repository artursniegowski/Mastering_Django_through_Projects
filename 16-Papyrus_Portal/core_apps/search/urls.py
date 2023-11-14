"""
urls mapping for the ElasticSearch.
"""
from django.urls import path

from .views import ArticleElasticSearchView

app_name = "search"

urlpatterns = [
    path(
        "search/",
        ArticleElasticSearchView.as_view(
            {"get": "list"}  # maps the HTTP get method to the list action
        ),
        name="article_search",
    ),
]
