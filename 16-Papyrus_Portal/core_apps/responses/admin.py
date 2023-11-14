"""
Django admin  - Responses.
"""
from django.contrib import admin

from .models import Response


class ResponseAdmin(admin.ModelAdmin):
    """Define the admin pages for Responses."""

    list_display = [
        "id",
        "pkid",
        "user",
        "article",
        "parent_response",
        "content",
        "created_at",
        "updated_at",
    ]
    list_display_links = [
        "pkid",
        "id",
        "user",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]


admin.site.register(Response, ResponseAdmin)
