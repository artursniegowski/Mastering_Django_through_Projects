"""
Serializer for the Article, ArticleView api
"""
from rest_framework import serializers

from core_apps.articles.models import Article, ArticleView, Clap
from core_apps.bookmarks.models import Bookmark
from core_apps.bookmarks.serializers import BookmarkSerializer
from core_apps.profiles.serializers import ProfileSerializer
from core_apps.responses.serializers import ResponseSerializer


# creating a custom tag list field class that allows you to handle
# tags as a list of strings, it will properly convert the input
# tag instance when creating or updating an article and vice versa
class TagListField(serializers.Field):
    """allow us to handle tags as list of strings"""

    # the value is the tags field from the article model
    def to_representation(self, value):
        """returning a list of tag names by iterating over all of the tags
        associated with the articles"""
        return [tag.name for tag in value.all()]

    # data is the tags field from the request data
    def to_internal_value(self, data):
        if not isinstance(data, list):
            raise serializers.ValidationError("Expected a list of tags")
        tag_objects = []
        for tag_name in data:
            # removes any leading or trailing white spaces from the tag name
            tag_name = tag_name.strip()

            if not tag_name:
                continue

            tag_objects.append(tag_name)

        return tag_objects


class ArticleSerializer(serializers.ModelSerializer):
    """Model serializer for Article"""

    author_info = ProfileSerializer(source="author.profile", read_only=True)
    banner_image = serializers.SerializerMethodField()
    estimated_reading_time = serializers.ReadOnlyField()
    tags = TagListField()
    views = serializers.SerializerMethodField()
    average_rating = serializers.ReadOnlyField()
    bookmarks = serializers.SerializerMethodField()
    bookmarks_count = serializers.SerializerMethodField()
    claps_count = serializers.SerializerMethodField()
    responses = ResponseSerializer(many=True, read_only=True)
    responses_count = serializers.IntegerField(source="responses.count", read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_responses_count(self, obj):
        """returning the responses count"""
        return obj.responses.count()

    def get_claps_count(self, obj):
        """returning the claps count"""
        return obj.claps.count()

    def get_bookmarks(self, obj):
        """returning the bookmarks serilized data"""
        bookmarks = Bookmark.objects.filter(article=obj)
        return BookmarkSerializer(bookmarks, many=True).data

    def get_bookmarks_count(self, obj):
        """returning the number of bookmarks"""
        return Bookmark.objects.filter(article=obj).count()

    def get_average_rating(self, obj):
        """returns the average rating for a given article"""
        # adding the average rating field to our article serializer
        # and also include the average rating in the serializer output
        return obj.average_rating()

    def get_views(self, obj):
        return ArticleView.objects.filter(article=obj).count()

    def get_banner_image(self, obj):
        return obj.banner_image.url

    def get_created_at(self, obj):
        now = obj.created_at
        formated_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formated_date

    def get_updated_at(self, obj):
        now = obj.updated_at
        formated_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formated_date

    # the string related field for the tags is read only by default but if we want
    # to allow adding or updating tags when creating or updating an article
    # so we need to implement a custom create and update method
    # we achive this by overiding the create and update method
    def create(self, validated_data):
        tags = validated_data.pop("tags")
        article = Article.objects.create(**validated_data)
        article.tags.set(tags)
        return article

    def update(self, instance, validated_data):
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.body = validated_data.get("body", instance.body)
        instance.banner_image = validated_data.get(
            "banner_image", instance.banner_image
        )
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)

        if "tags" in validated_data:
            instance.tags.set(validated_data["tags"])
        instance.save()
        return instance

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "tags",
            "estimated_reading_time",
            "author_info",
            "views",
            "description",
            "body",
            "banner_image",
            "average_rating",
            "bookmarks",
            "bookmarks_count",
            "claps_count",
            "responses",
            "responses_count",
            "created_at",
            "updated_at",
        ]


class ClapSerializer(serializers.ModelSerializer):
    """Model serializer for Clap"""

    article_title = serializers.CharField(source="article.title", read_only=True)
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)

    class Meta:
        model = Clap
        fields = [
            "id",
            "article_title",
            "user_first_name",
        ]
