"""
Serializer for the Profile app
"""
from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Model serializer for Profile"""

    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    # read only means the field shoul only be serializeed but not deserialized
    full_name = serializers.SerializerMethodField(read_only=True)
    profile_photo = serializers.SerializerMethodField()
    country = CountryField(name_only=True)  # only country names

    class Meta:
        model = Profile
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "profile_photo",
            "phone_number",
            "gender",
            "country",
            "city",
            "twitter_handle",
            "about_me",
        ]

    def get_full_name(self, obj: Profile):
        """returing the full name method - serialized"""
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_profile_photo(self, obj: Profile):
        """returing the profile photo method - serialized"""
        return obj.profile_photo.url


class UpdateProfileSerializer(serializers.ModelSerializer):
    """serializer for updating the Profile"""

    country = CountryField(name_only=True)  # only country names

    class Meta:
        model = Profile
        # only fields in the list will be allowed to be updated by the user
        fields = [
            "profile_photo",
            "phone_number",
            "gender",
            "country",
            "city",
            "twitter_handle",
            "about_me",
        ]


class FollowingSerializer(serializers.ModelSerializer):
    """get the users following the currently logged in user."""

    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "profile_photo",
            "about_me",
            "twitter_handle",
        ]
