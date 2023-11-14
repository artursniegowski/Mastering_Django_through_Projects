"""
Django admin  - Profile model.
"""
from django.contrib import admin

from .forms import ProfileForm
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """Define the admin pages for Profile."""

    # for extra validation of followers
    form = ProfileForm
    list_display = [
        "pkid",
        "id",
        "user",
        "gender",
        "phone_number",
        "country",
        "city",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    list_display_links = ["pkid", "id", "user"]
    list_filter = ["id", "pkid"]


admin.site.register(Profile, ProfileAdmin)
