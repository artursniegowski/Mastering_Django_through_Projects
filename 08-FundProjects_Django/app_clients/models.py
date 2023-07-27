from django.db import models

# One client has many users ! 
class Client(models.Model):
    company = models.CharField(max_length=250,unique=True, blank=False)
    name = models.CharField(max_length=250,unique=True, blank=False)
    descritpion = models.TextField(max_length=2000, blank=True)

    def __str__(self) -> str: 
        return self.company 
 
