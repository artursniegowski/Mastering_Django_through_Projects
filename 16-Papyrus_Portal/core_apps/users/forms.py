"""
Customizing forms for the user.
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import (
    BaseUserCreationForm as BaseUserCreationFormOriginal,  # UserCreationForm,
)
from django.contrib.auth.forms import UserChangeForm as UserChangeFormOriginal

User = get_user_model()


# we use same name so we dont have to explicitly specify them
# in the admin pannel as add_form
class UserChangeForm(UserChangeFormOriginal):
    """Form for changing custom user"""

    class Meta:
        model = User
        exclude = ("username",)
        # fields = ('email', 'password1', 'password2')


# we use same name so we dont have to explicitly specify them
# in the admin pannel as form
class UserCreationForm(BaseUserCreationFormOriginal):
    """Form for creatingthe custom user"""

    class Meta:
        model = User
        fields = ("email",)

    # no need for clean_email since the email field is defined
    # as unique and django build in validation form will handl this


class UserLoginForm(AuthenticationForm):
    """Form for authenticting the user"""

    class Meta:
        model = User
        fields = ("email", "password")
