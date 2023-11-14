"""
Serializers for the users app.
"""
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError as DjangoValidationError
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Seriazlizer for the user object."""

    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ReadOnlyField(source="profile.profile_photo.url")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "gender",
            "phone_number",
            "profile_photo",
            "country",
            "city",
        ]
        # extra_kwargs = {
        #     'password': {'write_only': True, 'min_length': 5},
        # }

    def to_representation(self, instance):
        """adding the admin field to the serialized data
        it will only show the admin field if the user is an admin
        """
        representation = super().to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation


class CustomRegisterSerializer(RegisterSerializer):
    """Creating the custom resgister serializer"""

    username = None  # bc we are not using any username in our appllication
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        """retriving the cleaned or validated data from the serializer
        after it has been processed by the validation and cleaning methods
        """
        super().get_cleaned_data()
        # returning a dictionary containing the cleaned data witht he keys
        # matching the field names defined in this serializer
        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data["password1"], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
                )
        user.save()
        setup_user_email(request, user, [])
        user.email = self.cleaned_data.get("email")
        user.password = self.cleaned_data.get("password1")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        return user
