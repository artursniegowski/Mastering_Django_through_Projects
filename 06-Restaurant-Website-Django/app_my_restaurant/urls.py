from django.urls import path
from . import views

app_name = 'app_my_restaurant'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>', views.display_menu_item, name='menu_item'),
]