"""
Tests for the Users serializers
"""
import pytest
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from core_apps.users.serializers import CustomRegisterSerializer, UserSerializer

User = get_user_model()


@pytest.mark.django_db
def test_user_serializer(normal_user):
    """testing fields form the user serializer"""
    serializer = UserSerializer(normal_user)
    assert "id" in serializer.data
    assert "email" in serializer.data
    assert "first_name" in serializer.data
    assert "last_name" in serializer.data
    assert "gender" in serializer.data
    assert "phone_number" in serializer.data
    assert "profile_photo" in serializer.data
    assert "country" in serializer.data
    assert "city" in serializer.data


@pytest.mark.django_db
def test_to_representation_normal_user_serializer(normal_user):
    """testing to_representation method from the user serializer for regualr user"""
    serializer = UserSerializer(normal_user)
    assert "admin" not in serializer.data


@pytest.mark.django_db
def test_to_representation_super_user_serializer(super_user):
    """testing to_representation method from the user serializer for super user"""
    serializer = UserSerializer(super_user)
    assert "admin" in serializer.data


@pytest.mark.django_db
def test_custom_registration_user_serializer(mock_request):
    """testing fields form the custom user serializer"""
    valid_data = {
        "email": "test@test.com",
        "first_name": "Tim",
        "last_name": "lastExampleName",
        "password1": "testpassword",
        "password2": "testpassword",
    }
    serializer = CustomRegisterSerializer(data=valid_data)
    assert serializer.is_valid()

    user = serializer.save(mock_request)
    assert user.email == valid_data["email"]
    assert user.first_name == valid_data["first_name"]
    assert user.last_name == valid_data["last_name"]

    invalid_data = {
        "email": "test@test.com",
        "first_name": "Tim",
        "last_name": "lastExampleName",
        "password1": "testpassword",
        "password2": "testpassword2_wrong",
    }

    serializer = CustomRegisterSerializer(data=invalid_data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
