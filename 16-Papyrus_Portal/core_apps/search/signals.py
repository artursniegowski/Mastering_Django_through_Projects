"""
Signal file, for ElasticSearch.
"""
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry

from core_apps.articles.models import Article


@receiver(post_save, sender=Article)
def update_document(sender, **kwargs):
    """Updates the registry with the Article instance whenever
    save on this model happens"""
    # updating ArticleDocument in elasticsearch
    registry.update(kwargs["instance"])


@receiver(post_delete, sender=Article)
def delete_document(sender, **kwargs):
    """delete the ArticleDocument in ElastiSearch when the
    article instance is deleted"""
    registry.delete(kwargs["instance"])
