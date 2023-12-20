"""
Bookmarks model.
"""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.articles.models import Article


class Bookmark(models.Model): 
    """Bookmark model"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookmarks",
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="bookmarks",
    )
    created_at = models.DateTimeField(
        _("created"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Bookmark")
        verbose_name_plural = _("Bookmarks")
        unique_together = ["user", "article"]
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user.first_name} bookmarked {self.article.title}"
