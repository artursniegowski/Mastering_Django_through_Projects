"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from restaurant.views import intro
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # intro to the website
    path('', intro),
    path('restaurant/',include('restaurant.urls_main')),
    path('api/',include('restaurant.urls')),
    # path('restaurant/booking/', include(booking_router.urls)),
    # adding djoser endpoints for authentication
    # https://djoser.readthedocs.io/en/latest/getting_started.html
    path('api/registration/', include('djoser.urls')),
    path('api/registration/', include('djoser.urls.authtoken')),
    # for token authentication - djoser already gives that functionality
    # so this is kind of repetition
    # path('api-token-auth/', obtain_auth_token),

]
