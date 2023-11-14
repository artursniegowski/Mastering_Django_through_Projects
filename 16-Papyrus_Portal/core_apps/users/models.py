"""
User model.
"""
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Custom deffined User in the system"""

    # pseudo primary key - used so we can faster filter by the users pkid
    pkid = models.BigAutoField(primary_key=True, editable=False)
    # this is our id field used for the User model
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(verbose_name=_("first name"), max_length=75)
    last_name = models.CharField(verbose_name=_("last name"), max_length=75)
    email = models.EmailField(
        _("email address"),
        db_index=True,
        max_length=255,
        unique=True,
        blank=False,
        help_text=_("Required. It has to be a valid email, max 255 characters."),
        error_messages={
            "unique": _("This email address already exists."),
        },
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta(AbstractBaseUser.Meta):
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self) -> str:
        """returns the string representation of the user"""
        return self.email

    @property
    def get_full_name(self) -> str | None:
        """return the full name"""
        if self.first_name and self.last_name:
            return f"{self.first_name.title()} {self.last_name.title()}"
        return None

    @property
    def get_short_name(self) -> str | None:
        """returns the first name"""
        if self.first_name:
            return self.first_name
        return None
