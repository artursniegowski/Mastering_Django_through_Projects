from django.urls import path
from . import views

urlpatterns = [
    # ex: api/
    # main page
    path('', views.index),
    # ex: api/
    # GET: books  - list all books
    # POST: books - create a new book in the databse
    path('books',views.BooksView.as_view()),
    # ex: api/ 
    # GET: book/<int:pk> - get a single book
    # PUT: book/<int:pk> - unpdate a single book
    # PATCH: book/<int:pk> - partial update a single book
    # DELETE: book/<int:pk> - delete a single book
    path('book/<int:pk>',views.SingleBookView.as_view()),
]


