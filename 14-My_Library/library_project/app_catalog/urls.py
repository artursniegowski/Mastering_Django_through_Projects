from django.urls import path  # , include, re_path
from app_catalog import views

app_name = 'app_catalog'

urlpatterns = [
    # ex: catalog/
    path('', views.IndexView.as_view(), name='index'),
    path('book/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    # re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),  # noqa
    path('author/', views.AutorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),  # noqa
    path('mybooks/', views.LoanedBookByUserListView.as_view(), name='borrowed-books'),  # noqa
    path('borrowed/', views.AllBorrowedBooksByUserListView.as_view(), name='borrowed-all'),  # noqa
    path('book/<uuid:pk>/renew/', views.RenewBookLibrarianView.as_view(), name='renew-book-librarian'),  # noqa
    # authors path
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),  # noqa
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),  # noqa
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),  # noqa
    # books path
    path('book/create/', views.BookCreate.as_view(), name='book-create'),  # noqa
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),  # noqa
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),  # noqa
]
