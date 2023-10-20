from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
from restaurant.models import Booking, Menu
from restaurant.serializers import BookingSerializer, MenuSerializer
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'restaurant/index.html', {'current_year':datetime.datetime.now().year})

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'restaurant/about.html', {'current_year':datetime.datetime.now().year})

def menu(request: HttpRequest) -> HttpResponse:
    return render(request, 'restaurant/menu.html', {'current_year':datetime.datetime.now().year})

def book(request: HttpRequest) -> HttpResponse:
    return render(request, 'restaurant/book.html', {'current_year':datetime.datetime.now().year})

def intro(request: HttpRequest) -> HttpResponse:
    return render(request, 'restaurant/intro.html')

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]