from django.urls import path, include
from . import views
from rest_framework import routers

# tables/
# tables/<int:pk>
booking_router = routers.DefaultRouter()
booking_router.register(r'tables', views.BookingViewSet)

app_name = 'restaurant'

urlpatterns = [
    # path('', views.index, name='home'),
    # external: api/
    path('menu/items', views.MenuItemsView.as_view(), name='menu_items'),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('bookings/', include(booking_router.urls)),
]
