from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here. 
class Booking(models.Model):
    name = models.CharField(max_length=255)
    # max length 6 digits - chnged to more rational number like 0-999
    no_of_guests = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    bookingDate = models.DateField(db_index=True)

    def __str__(self) -> str:
        return f"Booking on the {self.bookingDate} for {self.no_of_guests} guests for name: {self.name}"

class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # max length 5 digits - chnged to more rational number like 0-9999
    inventory = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    
    def __str__(self) -> str:
        return f"{self.title}: {self.price:.2f}"
