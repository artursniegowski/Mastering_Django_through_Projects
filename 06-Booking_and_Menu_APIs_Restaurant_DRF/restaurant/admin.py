from django.contrib import admin
from restaurant.models import Booking, Menu

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    pass

class MenuAdmin(admin.ModelAdmin):
    pass

admin.site.register(Booking, BookingAdmin)
admin.site.register(Menu, MenuAdmin)