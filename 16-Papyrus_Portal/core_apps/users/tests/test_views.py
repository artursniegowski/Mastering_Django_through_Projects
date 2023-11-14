"""
Tests for the User Views
"""
import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core_apps.users.views import CustomUserDetailsView

User = get_user_model()


@pytest.mark.django_db
def test_authentication_required(normal_user):
    """testing that authnetication is required view"""
    client = APIClient()
    url = reverse("user_details")
    response = client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user=normal_user)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_retrive_user_detail(normal_user):
    """testing view to retrive user details"""
    client = APIClient()
    client.force_authenticate(user=normal_user)
    url = reverse("user_details")

    res = client.get(url)
    assert res.status_code == status.HTTP_200_OK
    assert res.data["email"] == normal_user.email
    assert res.data["first_name"] == normal_user.first_name
    assert res.data["last_name"] == normal_user.last_name


@pytest.mark.django_db
def test_update_user_details(normal_user):
    """testing view to update user details"""
    client = APIClient()
    client.force_authenticate(user=normal_user)
    url = reverse("user_details")

    new_first_name = "newFirstName"
    new_last_name = "newLastName"
    updated_data = {
        "first_name": new_first_name,
        "last_name": new_last_name,
    }

    res = client.patch(url, updated_data)
    assert res.status_code == status.HTTP_200_OK
    assert res.data["first_name"] == new_first_name
    assert res.data["last_name"] == new_last_name

    # checking if the cahnges were saved to database
    updated_user = User.objects.get(pk=normal_user.pk)
    assert updated_user.first_name == new_first_name
    assert updated_user.last_name == new_last_name


def test_get_queryset_empty(normal_user):
    """tessting getting an empty queryset"""
    client = APIClient()
    client.force_authenticate(user=normal_user)
    url = reverse("user_details")
    res = client.get(url)

    view = CustomUserDetailsView()
    view.request = res.wsgi_request

    queryset = view.get_queryset()
    assert queryset.count() == 0
