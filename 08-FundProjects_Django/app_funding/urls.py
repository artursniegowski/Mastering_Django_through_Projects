from django.urls import path
from . import views

app_name = 'app_funding'

urlpatterns = [
    # ex: ''
    path('', views.HomePageView.as_view(), name='home'),
    path('projekt/<int:pk>/', views.DetailProjectView.as_view(), name='detail-project'),
    # ex: '' 
    path('booking/<int:booking_id>/reactivate-request/', views.ReactivateBookingView.as_view() ,name='booking-reactivate-request'),
    path('booking/<int:follower_id>/book-request/', views.RequestBookingView.as_view() ,name='booking-request'),
    # ex: '' 
    path('project/<int:project_pk>/follow/', views.ProjectFollowView.as_view() ,name='follow'),
    # ex: ''
    path('extend-booking/<uuid:token>/', views.ExtendBookingView.as_view(), name='extend-booking'),
]