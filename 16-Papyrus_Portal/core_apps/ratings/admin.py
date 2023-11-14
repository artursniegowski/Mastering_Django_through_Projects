"""
Django admin  - Rating.
"""
from django.contrib import admin

from .models import Rating


class RatingAdmin(admin.ModelAdmin):
    """Define the admin pages for Rating."""

    list_display = [
        "id",
        "user",
        "article",
        "rating",
        "created_at",
        "updated_at",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]


admin.site.register(Rating, RatingAdmin)
