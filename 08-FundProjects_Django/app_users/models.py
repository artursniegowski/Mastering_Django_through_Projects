from django.db import models
from django.contrib.auth.models import AbstractUser


# TODO: explanation
# another way achive this is by craeting another model like Profile taht owuld have a one to one
# relationship to the user and we could add fields in taht model,
# and on top of taht we could add singals co create thei porfile whenever a user is created and vice versa
# but this is not recomded by django , as best optio is to use your own cusomized user by inheriting from abstractuser as shown 
# in this example 
# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class User(AbstractUser):
    """my custom user - that inherits from django user evertyhing 
    and only adding the client relationship"""  
    # adding a relationship, each client can have multiple users 
    # one - to many 
    client = models.ForeignKey('app_clients.Client', on_delete=models.SET_NULL, null=True, blank=True, related_name='clients')  
