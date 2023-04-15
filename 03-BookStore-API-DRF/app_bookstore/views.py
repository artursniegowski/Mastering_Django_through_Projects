from django.http import HttpRequest, HttpResponse
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BooksView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateAPIView ,generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# main page view            
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Welcome to the BOOK API.</h1>")