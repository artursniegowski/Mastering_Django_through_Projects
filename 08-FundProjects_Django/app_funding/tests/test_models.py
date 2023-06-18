from django.test import TestCase
from django.utils import timezone
from app_funding.models import Project, Booking, Follower, Token
from django.contrib.auth import get_user_model


class ProjectModelTestCase(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create(username='testuser')
        self.project = Project.objects.create(name='Test Project', description='Test Description', project_money_total=1000)
    
    def test_get_total_bookings(self):
        self.assertEqual(self.project.get_total_bookings, 0)
        # Create bookings for the project
        Booking.objects.create(user=self.user, project=self.project, booking_amount_money=100) 
        Booking.objects.create(user=self.user, project=self.project, booking_amount_money=200)
        self.assertEqual(self.project.get_total_bookings, 2)
    
    def test_get_all_valid_bookings(self):
        # Create bookings with different expiration dates
        booking1 = Booking.objects.create(user=self.user, project=self.project, booking_amount_money=100)
        booking2 = Booking.objects.create(user=self.user, project=self.project, booking_amount_money=200)
        booking2.booking_date = timezone.now() - timezone.timedelta(days=61)  # Expired booking
        booking2.save()
        
        valid_bookings = self.project.get_all_valid_bookings
        self.assertIn(booking1, valid_bookings)
        self.assertNotIn(booking2, valid_bookings)
    
    # TODO
    # Add more test for other properties and methods of the model

class BookingModelTestCase(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.project = Project.objects.create(name='Test Project', description='Test Description', project_money_total=1000)
        self.user = self.user_model.objects.create(username='testuser')
    
    def test_is_booking_expired(self):
        booking = Booking.objects.create(user=self.user, project=self.project, booking_amount_money=100)
        self.assertFalse(booking.is_booking_expired)
        
        # Set an expired booking date
        booking.booking_date = timezone.now() - timezone.timedelta(days=61)
        booking.save()
        self.assertTrue(booking.is_booking_expired)
    
    # TODO
    # Add more test for other properties and methods of the model

# TODO:
# Write similar test cases for other models (Follower, Token)
