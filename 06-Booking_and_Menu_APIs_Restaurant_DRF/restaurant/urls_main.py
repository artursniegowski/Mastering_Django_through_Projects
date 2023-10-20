from django.urls import path
from . import views

app_name = 'restaurant_main'

urlpatterns = [
    # ex: restaurant/
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
]