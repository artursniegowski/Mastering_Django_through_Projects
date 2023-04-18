from django.db import models

# Create your models here.
class Booking(models.Model):
    """representation of a booking table"""
    name = models.CharField(max_length=150)
    date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    
    class Meta: 
        unique_together = ('date', 'reservation_slot')
    
    def __str__(self) -> str:
        return f"{self.name} has a reservation on {self.date} for slot {self.reservation_slot}"
