from django.forms import ModelForm
from django import forms
from app_booking.models import Booking

SLOT_CHOICES = [
    (0, 'Select Time'),
    (10, '10:00 AM'),
    (11, '11:00 AM'),
    (12, '12:00 PM'),
    (13, '1:00 PM'),
    (14, '2:00 PM'),
    (15, '3:00 PM'),
    (16, '4:00 PM'),
    (17, '5:00 PM'),
    (18, '6:00 PM'),
    (19, '7:00 PM'),
    (20, '8:00 PM'),
]

class BookingForm(ModelForm):
    reservation_slot = forms.ChoiceField(choices=SLOT_CHOICES, initial=SLOT_CHOICES[0])
    
    class Meta:
        model = Booking
        fields = "__all__"
        
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                }),
            'reservation_slot': forms.Select(
                choices=SLOT_CHOICES,            
            ),
        }
        labels = {
            'date': 'Reservation date:',
            'reservation_slot': 'Select a slot:',
        }
        
    def clean_reservation_slot(self):
        """additonal check if the selected time slot is one that we defined !"""
        slot = int(self.cleaned_data.get('reservation_slot'))
        if slot == 0:
            raise forms.ValidationError("Please select a valid time slot.")
        elif slot < 10 or slot > 20:
            raise forms.ValidationError("Time slot must be between 10:00 AM and 8:00PM.")
        return slot