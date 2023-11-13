from app_add_models.models import UserModel
from django.core.exceptions import ValidationError
from django import forms
from sqlalchemy_test.settings import SA_DB_SESSION

    

class UserForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        max_length=100, 
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'maxlength': 200, 'class': 'form-control', 'rows':"3"}), 
        required=False
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        with SA_DB_SESSION() as db_session:
            if db_session.query(UserModel).filter_by(email=email).first():
                raise ValidationError('This email address is already in use.')
        return email
    
