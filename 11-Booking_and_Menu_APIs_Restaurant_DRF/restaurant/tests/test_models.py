from django.test import TestCase
from restaurant.models import Menu, Booking
from django.utils import timezone
from django.core.exceptions import ValidationError

# simple model Menu test
class MenuModelTest(TestCase):
    def test_output_model(self):
        item = Menu.objects.create(
            title = "IceCream",
            price = 2.50,
            inventory = 100,
        )
        string_output = str(item)
        # print(string_output)
        self.assertEqual(string_output, "IceCream: 2.50")
        
class BookingModelTest(TestCase):
    def test_output_model(self):
        new_booking = Booking.objects.create(
            name="Mike",
            no_of_guests = 2,
            bookingDate = timezone.now().date()
        )  

        self.assertEqual(new_booking.name, "Mike")
        self.assertEqual(new_booking.no_of_guests, 2)
        self.assertEqual(new_booking.bookingDate, timezone.now().date())
        
    def test_no_of_guests_validation(self):
        with self.assertRaises(ValidationError):
            new_booking = Booking.objects.create(
                name="Mike",
                no_of_guests = 1000,
                bookingDate = timezone.now().date()
            )  
            new_booking.full_clean()