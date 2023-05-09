from django.urls import path
from . import views

app_name = 'app_add_models'

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='home'),
    path('add/', views.AddCreateView.as_view(), name='add'),
    path('delete/<int:pk>/', views.DeleteUserView.as_view(), name='delete_user'),
]
