from django import forms
from django.contrib import admin
from app_catalog.models import (
    Author,
    Book,
    BookInstance,
    Genre,
    Language,
)


class BookInline(admin.StackedInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')  # noqa
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BookInline]


admin.site.register(Author, AuthorAdmin)


class BookInstanceInlineForm(forms.ModelForm):
    # only way making the custom id readonly in the TabularInline!
    class Meta:
        model = BookInstance
        fields = '__all__'
        widgets = {
            'id': forms.TextInput(attrs={'readonly': 'readonly', 'size':'36', 'style':'border:none;background:none;'}),  # noqa
        }


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    form = BookInstanceInlineForm
    extra = 0
    # fields = ('book', 'imprint', 'due_back', 'status')
    # readonly_fields = ('status',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    # this could also be dfined at model.py class Book,
    # then we dont need the obj, and we refer to the book as self!
    @admin.display(description="Genre")
    def display_genre(self, obj: Book):
        """
        Create  a string for the Genre. This is req to display genre in Admin.
        """
        return ', '.join(genre.name for genre in obj.genre.all()[:3])
    # display_genre.short_description = 'Genre'

    inlines = [BookInstanceInline]


admin.site.register(Book, BookAdmin)


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id', 'borrower', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    readonly_fields = ['id']

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)
