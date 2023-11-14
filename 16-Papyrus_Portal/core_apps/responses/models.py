"""
Responses model.
"""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.articles.models import Article
from core_apps.common.models import TimeStampedModel


class Response(TimeStampedModel):
    """Response model"""

    # user who wrote the resposne
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="responses"
    )
    # article asociated with the response
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="responses",
    )
    # used to store replies to other responses
    # if a response is a reply to another response,
    # it will store the parent response
    # if a response is not replay to another response, it will be null
    parent_response = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="replies",
        null=True,
        blank=True,
    )
    content = models.TextField(_("response content"))

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user.first_name} commented on {self.article.title}"
