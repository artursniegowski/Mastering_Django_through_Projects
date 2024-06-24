import pytest
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory
from pytest_factoryboy import register

from core_apps.users.tests.factories import UserFactory

# by registering UserFactory
# we can now use the user_factory fixture in our tests
register(UserFactory)


# the fixture creates a normal user using the user_factory
# which is an instace of the registered user factory
# the db - is a built in Pytest Django fixture that ensures
# the test database is set up correctly
@pytest.fixture
def normal_user(db, user_factory):
    """returns a newly created 'regular' user instace"""
    new_user = user_factory.create()
    return new_user


@pytest.fixture
def super_user(db, user_factory):
    """returns a newly created 'super' user instace"""
    new_user = user_factory.create(is_superuser=True, is_staff=True)
    return new_user


# mock fixture for HTTP requests
# this allows to simulate incoming HTTP request
# necessary beacuase our register serializer makes HTTP request to create a user
# when used in our views
@pytest.fixture
def mock_request():
    factory = RequestFactory()
    request = factory.get("/")
    middleware = SessionMiddleware(lambda req: None)
    middleware.process_request(request)
    request.session.save()

    auth_middleware = AuthenticationMiddleware(lambda req: None)
    auth_middleware.process_request(request)

    return request
