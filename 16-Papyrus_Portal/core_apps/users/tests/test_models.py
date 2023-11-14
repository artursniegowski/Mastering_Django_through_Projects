"""
Test for users models and managers
"""
import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

User = get_user_model()


# this decorator ensures that the test has access to the database
# and it handles any necesary setup and teardown of the test database
# normal_user - argument comes from the fixture we created - conftest.py
@pytest.mark.django_db
def test_create_normal_user(normal_user):
    """creating a new user test - checking if the fields are defined"""
    assert normal_user.first_name is not None
    assert normal_user.last_name is not None
    assert normal_user.email is not None
    assert normal_user.password is not None
    assert normal_user.pkid is not None
    assert not normal_user.is_staff
    assert not normal_user.is_superuser
    assert normal_user.is_active


@pytest.mark.django_db
def test_create_super_user(super_user):
    """creating a new superuser test - checking if the fields are defined"""
    assert super_user.first_name is not None
    assert super_user.last_name is not None
    assert super_user.email is not None
    assert super_user.password is not None
    assert super_user.pkid is not None
    assert super_user.is_staff
    assert super_user.is_superuser
    assert super_user.is_active


@pytest.mark.django_db
def test_get_full_name(normal_user):
    """testing the property get_full_name of the model"""
    full_name = normal_user.get_full_name
    expected_full_name = (
        f"{normal_user.first_name.title()} {normal_user.last_name.title()}"
    )
    assert full_name == expected_full_name


@pytest.mark.django_db
def test_get_full_name_if_first_name_and_last_name_empty(normal_user):
    """testing the property get_full_name of the model if first_name and last_name not defined"""
    normal_user.first_name = ""
    normal_user.last_name = ""
    normal_user.save()
    assert normal_user.get_full_name is None


@pytest.mark.django_db
def test_get_short_name(normal_user):
    """testing the property get_short_name of the model"""
    assert normal_user.get_short_name == normal_user.first_name


@pytest.mark.django_db
def test_get_short_name_if_first_name_not_defined(normal_user):
    """testing the property get_short_name of the model if first_name not defined"""
    normal_user.first_name = ""
    normal_user.save()
    assert normal_user.get_short_name is None


@pytest.mark.django_db
def test_update_user(normal_user):
    """testing updating user model"""
    new_first_name = "Sam"
    new_last_name = "Dam"
    normal_user.first_name = new_first_name
    normal_user.last_name = new_last_name
    normal_user.save()

    updated_user = User.objects.get(pk=normal_user.pk)
    assert updated_user.first_name == new_first_name
    assert updated_user.last_name == new_last_name


@pytest.mark.django_db
def test_delete_user(normal_user):
    """testing deleting a normal user"""
    user_pk = normal_user.pk
    normal_user.delete()

    with pytest.raises(User.DoesNotExist):
        User.objects.get(pk=user_pk)


@pytest.mark.django_db
def test_user_str(normal_user):
    """testing the string representation of a normal user"""
    assert normal_user.email == str(normal_user)


@pytest.mark.django_db
def test_normal_user_email_normalized(normal_user):
    """testing a new user email is normalized"""
    email = normal_user.email
    assert email == email.lower()


@pytest.mark.django_db
def test_super_user_email_normalized(super_user):
    """testing a super user email is normalized"""
    email = super_user.email
    assert email == email.lower()


@pytest.mark.django_db
def test_normal_user_invalid_email(user_factory):
    """testing an invalid email raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email="invalidEmail.com")
    assert str(err.value) == "You must provide a valid email address."


@pytest.mark.django_db
def test_normal_user_missing_email(user_factory):
    """testing missing email raises an error - normal user"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "The given email must be set"


@pytest.mark.django_db
def test_super_user_missing_email(user_factory):
    """testing missing email raises an error - superuser"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "The given email must be set"


@pytest.mark.django_db
def test_super_user_empty_password_created_login_fail(client, user_factory):
    """testing missing password superuser create -> login has to fail but the user should get created"""
    # user with empty password
    # shoudl get created but wont be able to login
    user = user_factory.create(password=None, is_superuser=True, is_staff=True)
    # attempt to log in witht he empty password
    login_successful = client.login(username=user.email, password=None)
    # assert that the login failed
    assert not login_successful


@pytest.mark.django_db
def test_super_user_is_not_staff(user_factory):
    """testing creating a super user that is not staff will rais an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superuser must have is_staff=True."


@pytest.mark.django_db
def test_super_user_is_not_superuser(user_factory):
    """testing creating a super user that is not superuser will rais an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == "Superuser must have is_superuser=True."


@pytest.mark.django_db
def test_with_perm_user_has_permission(normal_user):
    """Test that with_perm returns the user with a specific permission."""
    # retrive a permission
    permission = Permission.objects.get(codename="view_bookmark")
    normal_user.user_permissions.add(permission)
    # use the with_perm to check for the users with the given permission
    users_with_perm = User.objects.with_perm(
        permission, backend="django.contrib.auth.backends.ModelBackend"
    )
    assert normal_user in users_with_perm


@pytest.mark.django_db
def test_with_perm_user_lacks_permission(normal_user):
    """Test that with_perm does not return the user without a specific permission."""
    # retrive a permission
    permission = Permission.objects.get(codename="add_user")
    # Use with_perm to check for the permission
    users_with_perm = User.objects.with_perm(
        permission, backend="django.contrib.auth.backends.ModelBackend"
    )

    # Assert that the user is not in the result set
    assert normal_user not in users_with_perm


@pytest.mark.django_db
def test_with_perm_include_superusers(super_user):
    """Test that with_perm includes superusers if requested."""
    permission = Permission.objects.get(codename="add_user")
    # Use with_perm to check for a permission, including superusers
    users_with_perm = User.objects.with_perm(
        permission,
        include_superusers=True,
        backend="django.contrib.auth.backends.ModelBackend",
    )

    # Assert that the superuser is in the result set
    assert super_user in users_with_perm


@pytest.mark.django_db
def test_with_perm_exclude_superusers(super_user):
    """Test that with_perm excludes superusers if not requested."""
    permission = Permission.objects.get(codename="add_user")
    # Use with_perm to check for a permission, excluding superusers
    users_with_perm = User.objects.with_perm(
        permission,
        include_superusers=False,
        backend="django.contrib.auth.backends.ModelBackend",
    )

    # Assert that the superuser is not in the result set
    assert super_user not in users_with_perm
