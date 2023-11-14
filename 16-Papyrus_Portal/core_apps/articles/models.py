"""
Article model.
"""
from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from core_apps.common.models import TimeStampedModel

from .read_time_engine import ArticleReadTimeEngine


class Clap(TimeStampedModel):
    """Clap model"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        "Article",
        on_delete=models.CASCADE,
    )

    class Meta:
        # making sure a user can clap an article only once
        unique_together = ["article", "user"]
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user.first_name} clapped {self.article.title}"


class Article(TimeStampedModel):
    """Article model"""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    title = models.CharField(
        _("Title"),
        max_length=255,
    )
    slug = AutoSlugField(
        populate_from="title",
        always_update=True,
        unique=True,
    )
    description = models.CharField(
        _("description"),
        max_length=255,
    )
    body = models.TextField(
        _("article content"),
    )
    banner_image = models.ImageField(
        _("banner image"),
        default="/profile_default.png",
    )
    tags = TaggableManager()
    # representing th emany to many relationship between the user and
    # an article model
    # through this relationship a user can clap multiple articles
    # and an article can have clapps from multiple users
    # through is used to specify the model that will be used to create
    # many to many relatioship between the article and te user models
    claps = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through=Clap, related_name="clapped_articles"
    )

    def __str__(self) -> str:
        """String representation of the model"""
        return f"{self.author.first_name}'s article"

    @property
    def estimated_reading_time(self):
        """calulates the estimated reaing time for the article"""
        return ArticleReadTimeEngine.estimate_reading_time(self)

    def view_count(self):
        """return the view count for the article"""
        # using the reverse relationship
        return self.article_views.count()

    def average_rating(self):
        """raturns the average rating for the article"""
        # creating an method that is going to allow us to get the
        # average rating of an article
        ratings = self.ratings.all()
        if ratings.count() > 0:
            total_rating = sum(rating.rating for rating in ratings)
            average_rating = total_rating / ratings.count()
            return round(average_rating, 2)
        return None


class ArticleView(TimeStampedModel):
    """ArticleView model - for counting the views,
    it hepls tracking what article, was viewwed by whi and what was
    the IP address, if the IP address does not exists the user will be
    declared as Annonymous
    """

    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="article_views"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # when the reference object is deleted, the objects that have
        # references to it hsould be set to null
        on_delete=models.SET_NULL,
        # is set to nullabel to allow for anonymous views
        null=True,
        related_name="user_views",
    )
    viewer_ip = models.GenericIPAddressField(
        _("viewer IP"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Article View")
        verbose_name_plural = _("Article Views")
        unique_together = ("article", "user", "viewer_ip")

    def __str__(self) -> str:
        return f"{self.article.title} viewed by {self.user.first_name if self.user else 'Anonymous'} from IP {self.viewer_ip}"  # noqa

    @classmethod
    def record_view(cls, article, user, viewer_ip):
        # getting an existing instance of ArticleView or create one
        # given the article, user, viewer_ip
        # it reutnrs a tuple, a ArticleView instance and a bool indicating
        # weather the instance was created (true) or retrived (false)
        view, _ = cls.objects.get_or_create(
            article=article,
            user=user,
            viewer_ip=viewer_ip,
        )
        view.save()
