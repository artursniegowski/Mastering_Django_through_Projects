from app_funding.models import Token, Booking
from django.db.models.signals import post_save
from django.dispatch import receiver

# ensures that we creat a token for every booking that was created !
@receiver(post_save, sender=Booking)
def create_token(sender, **kwargs):
    """Create a new token for each created booking"""
    if kwargs["created"]:
        Token.objects.create(booking=kwargs["instance"])