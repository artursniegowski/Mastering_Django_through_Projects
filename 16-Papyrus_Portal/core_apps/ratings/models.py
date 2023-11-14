"""
Rating model.
"""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.articles.models import Article
from core_apps.common.models import TimeStampedModel


class Rating(TimeStampedModel):
    """Rating model"""

    RATING_CHOICES = [
        (1, _("Poor")),
        (2, _("Fair")),
        (3, _("Good")),
        (4, _("Very Good")),
        (5, _("Excellent")),
    ]
    article = models.ForeignKey(
        Article, related_name="ratings", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        _("rating"),
        choices=RATING_CHOICES,
    )
    review = models.TextField(_("review"), blank=True)

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")
        unique_together = ("article", "user")

    def __str__(self) -> str:
        return f"{self.user.first_name} rated {self.article.title} as {self.get_rating_display()}"
