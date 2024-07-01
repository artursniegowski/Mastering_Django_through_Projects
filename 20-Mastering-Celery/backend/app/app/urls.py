"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    # for serving files in development - only!!
    # not needed as media and static files served by nginx!
    # dont forget to run collectstatic to move all the static files!!
    # only needed if django service is accessed directly without nginx like
    # localhost:8000/api,  localhost:8000/
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # debug toolbar active in debug only
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

admin.site.site_header = "Mastering Celery"
admin.site.site_title = "Mastering Celery Portal"
admin.site.index_title = "Welcome to Mastering Celery Dashboard"
