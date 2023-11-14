"""
Test for users forms
"""
import pytest

from core_apps.users.forms import UserCreationForm
from core_apps.users.tests.factories import UserFactory


@pytest.mark.django_db
def test_user_creation_form_valid_data():
    """testing user creation form with valid data"""
    data = {
        "first_name": "Sam",
        "last_name": "Brum",
        "email": "sam.burm@noreplay.com",
        "password1": "secure_password_123",
        "password2": "secure_password_123",
    }
    form = UserCreationForm(data)
    assert form.is_valid()


@pytest.mark.django_db
def test_user_creation_form_invalid_data():
    """testing user creation form with invalid data"""
    user = UserFactory()

    data = {
        "first_name": "Samy",
        "last_name": "Brumy",
        "email": user.email,  # this should cause an error bc it already exists
        "password1": "secure_password_123",
        "password2": "secure_password_123",
    }
    form = UserCreationForm(data)
    assert not form.is_valid()
    assert "email" in form.errors
