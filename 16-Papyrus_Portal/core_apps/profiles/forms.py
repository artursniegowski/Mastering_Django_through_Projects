"""
Forms for Profile
"""
from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    """custom form for Profiles to prevent profile from following itself"""

    class Meta:
        model = Profile
        fields = "__all__"

    def clean_followers(self):
        """checking if Profile following itself, and preventing this behaviour"""
        followers = self.cleaned_data.get("followers")
        if self.instance and self.instance in followers.all():
            raise forms.ValidationError("A profile cannot follow itself.")
        return followers
