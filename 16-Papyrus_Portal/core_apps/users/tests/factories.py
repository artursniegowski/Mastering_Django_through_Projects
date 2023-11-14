"""
User model factory
"""
import factory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from faker import Factory as FakerFactory

faker = FakerFactory.create()
User = get_user_model()


# decorator used to mute the positive signal when creating
# instaces of the user model, this can be useful to avoid
# triggering any side effects that are connected to this signal
@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    """User model factory"""

    class Meta:
        model = User

    # generating random data for the fields - using faker
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    email = factory.LazyAttribute(lambda x: faker.email())
    password = factory.LazyAttribute(lambda x: faker.password())
    is_active = True
    is_staff = False

    # override the create method to customize the object creation process
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)
