"""
Django admin customization - custom user model.
"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
 
    # add_form = UserCreationForm  # no need to define as same name as default
    # form = UserChangeForm  # no need to define as same name as default
    ordering = ["email"]
    list_display = [
        "pkid",
        "id",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "date_joined",
    ]
    list_display_links = ["pkid", "id", "email"]
    list_filter = ["email", "is_staff", "is_active"]
    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password", "pkid", "id")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ["date_joined", "last_login", "id", "pkid"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    # 'first_name',
                    # 'last_name',
                    # 'is_staff',
                    # 'is_active',
                    # 'is_superuser',
                ),
            },
        ),
    )
    search_fields = ["email", "first_name", "last_name"]


admin.site.register(User, UserAdmin)
