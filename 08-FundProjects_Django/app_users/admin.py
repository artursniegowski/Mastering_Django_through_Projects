from app_users.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http.request import HttpRequest
from typing import Any, Callable, Optional, Sequence, Union

class CustomUserAdmin(UserAdmin):
    model = User
    
    fieldsets = UserAdmin.fieldsets + (
        ('Client', {'fields': ('client',)}),  
    )
    
admin.site.register(User,CustomUserAdmin)
