from django import forms
from django.forms import ModelForm
from app_funding.models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_amount_money'] 
        widgets = { 
            'booking_amount_money': forms.NumberInput(attrs={'min': 50, 'class': 'form-control', 'placeholder':'USD'}),
        }
        labels = { 
            'booking_amount_money': 'Your support amount, min 50.00$', 
        } 
