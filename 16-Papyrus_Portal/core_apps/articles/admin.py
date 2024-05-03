"""
Django admin  - Article, ArticleView model.
"""
from django.contrib import admin

from .models import Article, ArticleView, Clap


class ArticleAdmin(admin.ModelAdmin):
    """Define the admin pages for Article."""
 
    list_display = [
        "pkid",
        "author",
        "title",
        "slug",
        "view_count", 
    ] 
    list_display_links = ["pkid", "author"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title", "body", "tags"]
    ordering = ["-created_at"]


admin.site.register(Article, ArticleAdmin)


class ArticleViewAdmin(admin.ModelAdmin):
    """Define the admin pages for ArticleView."""

    list_display = [
        "pkid",
        "article",
        "user",
        "viewer_ip",
    ]
    list_display_links = ["pkid", "article"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["article", "user", "viewer_ip"]


admin.site.register(ArticleView, ArticleViewAdmin)


class ClapAdmin(admin.ModelAdmin):
    """Define the admin pages for Clap."""

    list_display = [
        "pkid",
        "id",
        "user",
        "article",
    ]
    list_display_links = ["id", "user"]
    list_filter = ["created_at", "updated_at"]


admin.site.register(Clap, ClapAdmin)
