from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    """for customization"""
    pass

admin.site.register(Book, BookAdmin)