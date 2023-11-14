"""
ArticleDocument fro Elasticsearch
"""
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from core_apps.articles.models import Article


# used to register ArticleDocument with Django elasticsearch DSL
# this enables the framework to manage the Elasticsearch index for the article model
# https://django-elasticsearch-dsl.readthedocs.io/en/latest/quickstart.html#install-and-configure
@registry.register_document
class ArticleDocument(Document):
    # the fields here, will be indexed by Elasticsearch
    # the attr -> specifies which model field should be used as
    # a source of data for ElasticSearch - so title from Article model
    title = fields.TextField(attr="title")
    description = fields.TextField(attr="description")
    body = fields.TextField(attr="body")
    author_first_name = fields.TextField()
    author_last_name = fields.TextField()
    tags = fields.KeywordField()

    # this inner class specifies the index settings,
    # including the index name and Elasticsearch settings
    class Index:
        # Name of the Elasticsearch index
        name = "articles"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        # The model associated with this Document
        model = Article

        # The fields of the model you want to be indexed in Elasticsearch
        fields = ["created_at"]

    # preparing custom fields for indexing
    def prepare_author_first_name(self, instance):
        return instance.author.first_name

    def prepare_author_last_name(self, instance):
        return instance.author.last_name

    def prepare_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]
