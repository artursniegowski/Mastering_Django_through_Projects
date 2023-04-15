from django.contrib import admin
from app_booking.models import Booking
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Booking, BookingAdmin)