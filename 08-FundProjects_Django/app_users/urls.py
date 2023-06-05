from django.urls import path
from .views import LoginUserView, LogoutUserView

app_name = 'app_users'

urlpatterns = [
    # ex 'users/'
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]