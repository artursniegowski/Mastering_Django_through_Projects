from django.test import TestCase
from rest_framework import status
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.utils import timezone

class MenuViewTest(TestCase):
    
    def create_init_data(self):
        self.menu1 = Menu.objects.create( title = "Pizza",price = 25.25,inventory = 40)
        self.menu2 = Menu.objects.create( title = "Burger",price = 25.25,inventory = 40)
        self.menu3 = Menu.objects.create( title = "Fries",price = 25.25,inventory = 40)
    
        
    def create_user(self, username:str, password:str)-> User:
        return User.objects.create(username=username, password=password)
               
    def setUp(self) -> None:
        self.create_init_data()
        self.client = APIClient()
        # create a new user
        self.user = self.create_user("testUser","BigTestPasswordNot!$")
        # create a token for that user
        self.token = Token.objects.create(user=self.user)
        # adding token to the clients headers
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        
    def test_getall(self):
        response = self.client.get(reverse('restaurant:menu_items'))
        menu_items = Menu.objects.all()
        menu_items_serialized = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, menu_items_serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
class BookingViewTest(TestCase):
    
    def create_init_data(self):
        self.menu1 = Booking.objects.create(name="Mike",no_of_guests = 2,bookingDate = timezone.now().date())
        self.menu2 = Booking.objects.create(name="Mark",no_of_guests = 3,bookingDate = timezone.now().date())
        self.menu3 = Booking.objects.create(name="Sam",no_of_guests = 1,bookingDate = timezone.now().date())
    
        
    def create_user(self, username:str, password:str)-> User:
        return User.objects.create(username=username, password=password)
               
    def setUp(self) -> None:
        self.create_init_data()
        self.client = APIClient()
        # create a new user
        self.user = self.create_user("testUser","BigTestPasswordNot!$")
        # create a token for that user
        self.token = Token.objects.create(user=self.user)
        # adding token to the clients headers
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        
    def test_getall(self):
        response = self.client.get(reverse('restaurant:booking-list'))
        bookings_items = Booking.objects.all()
        bookings_items_serialized = BookingSerializer(bookings_items, many=True)
        self.assertEqual(response.data, bookings_items_serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)