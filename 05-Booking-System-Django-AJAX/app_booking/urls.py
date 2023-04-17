from django.urls import path
from . import views
app_name = 'app_booking'

urlpatterns = [
    # ex: '' 
    # home view
    path('', views.home, name='home'),
    # about view
    path('about/', views.about, name='about'),
    # about view
    path('book/', views.book, name='book'),
    # booking info 
    path('booking-info', views.booking_info, name='booking-info'),
    # all-bookings
    path('all-bookings', views.get_all_bookings, name='all-bookings'),
]
