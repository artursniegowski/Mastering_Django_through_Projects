"""
Signal file, handling post_save from User model.
"""
import logging

from django.conf import settings
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from core_apps.profiles.models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, **kwargs):
    """Creates a profile whenever a user is created"""
    if kwargs["created"]:
        Profile.objects.create(user=kwargs["instance"])
        logger.info(f"{kwargs['instance']}'s profile has been created.")


@receiver(m2m_changed, sender=Profile.followers.through)
def prevent_self_follow(sender, **kwargs):
    """prevents profiles from self following"""
    if kwargs["action"] == "pre_add" and kwargs["instance"].pk in kwargs["pk_set"]:
        raise ValueError("Signal: A profile cannot follow itself.")
