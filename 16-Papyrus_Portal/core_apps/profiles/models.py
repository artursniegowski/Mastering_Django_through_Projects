"""
Profile model.
"""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from core_apps.common.models import TimeStampedModel


class Profile(TimeStampedModel):
    """Profile model"""

    class Gender(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")
        OTHER = "O", _("Other")

    gender = models.CharField(
        _("gender"),
        max_length=1,
        choices=Gender.choices,
        default=Gender.OTHER,
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    phone_number = PhoneNumberField(
        _("phone number"),
        max_length=30,
        default="+496912345678",
    )
    about_me = models.TextField(
        _("about me"),
        default="say something about yourself",
    )
    country = CountryField(
        _("country"),
        default="DE",
        blank=False,
        null=False,
    )
    city = models.CharField(
        _("city"),
        max_length=180,
        default="Berlin",
        blank=False,
        null=False,
    )
    profile_photo = models.ImageField(
        _("profile photo"), default="/profile_default.png"
    )
    twitter_handle = models.CharField(
        _("twitter handle"),
        max_length=20,
        blank=True,
    )
    # Make sure you cant follow yourself !
    # symmetrical=False: By setting symmetrical to False, you are making the
    # relationship between Profile instances asymmetrical. This means that if
    # one Profile instance follows another (A follows B), it
    # doesn't automatically mean that B follows A
    followers = models.ManyToManyField(
        # referencing itself, so many to many relationship with other profiles
        "self",
        symmetrical=False,
        related_name="following",
        blank=True,
    )

    def __str__(self) -> str:
        """String representation of the model"""
        return f"{self.user.first_name}'s Profile"

    def follow(self, profile):
        """Following other profiles"""
        # disallowing following yourself
        if profile.id != self.id:
            self.followers.add(profile)
        else:
            raise ValueError(_("A profile cannot follow itself."))

    def unfollow(self, profile):
        """Unfollow the given porfile"""
        self.followers.remove(profile)

    def check_following(self, profile) -> bool:
        """check if the profiles follows a given porfile"""
        return self.followers.filter(pkid=profile.pkid).exists()
