"""
urls for the health check of the application
"""
from django.urls import path
from . import views

app_name = 'app_core'

urlpatterns = [
    # ex: health/
    path('health-check/', views.health_check, name='health-check'),
]
