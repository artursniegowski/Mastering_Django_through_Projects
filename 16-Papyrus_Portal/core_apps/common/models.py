"""
Defining models fields that are common acros multiple models.
"""
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """Abstact model for TimeStamp"""

    # pseudo primary key - used so we can faster filter by the pkid
    pkid = models.BigAutoField(primary_key=True, editable=False)
    # this is our id field
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(
        _("created"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("updated"),
        auto_now=True,
    )

    class Meta:
        # means that this class will not generate a table
        # but it will be used as a base class for another model
        abstract = True
        ordering = ["-created_at", "-updated_at"]
