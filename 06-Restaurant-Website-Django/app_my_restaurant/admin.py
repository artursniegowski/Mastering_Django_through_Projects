from django.contrib import admin
from .models import Menu, Booking

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    pass

class BookingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking, BookingAdmin)