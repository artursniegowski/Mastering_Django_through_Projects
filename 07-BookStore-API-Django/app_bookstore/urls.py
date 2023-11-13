from django.urls import path
from . import views

app_name = 'app_bookstore'

urlpatterns = [
    # ex: api/
    # main page
    path('', views.index, name='api_home'),
    # ex: api/
    # retreive all books , or create book if post
    path('books',views.books, name='get_books'),
    # ex: api/ 
    # delete and update or retrive a (single) book
    path('book/<int:pk>',views.book, name='book_alter'),
]


