from django.db import models

# Create your models here.
class Book(models.Model):
    """table representation for the books databse"""
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.PositiveSmallIntegerField(default=0) # max is 32767
    
    def __str__(self) -> str:
        return self.title +" by "+ self.author
    
    class Meta:
        # https://docs.djangoproject.com/en/4.1/ref/models/options/#indexes
        # to increase speed for data retreival and operations when called on these indexes
        indexes = [models.Index(fields=['price']),]