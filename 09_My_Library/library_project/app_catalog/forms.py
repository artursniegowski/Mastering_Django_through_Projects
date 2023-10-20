from datetime import date, timedelta
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from app_catalog.models import BookInstance


# class RenewBookForm(forms.Form):
#     """Form for renewing a book"""
#     renewal_date = forms.DateField(
#         help_text=_("Enter a date between now and 4 weeks (default 3).")
#     )

#     def clean_renewal_date(self):
#         """validating the renewal_date field"""
#         data = self.cleaned_data['renewal_date']

#         # check if date is in the future
#         if data < date.today():
#             raise ValidationError(_("Invalid date - renewal in the past"))

#         # check if the date is more than 4 weeks in the future
#         if data > (date.today() + timedelta(weeks=4)):
#             raise ValidationError(_("Invalid date - renewal more than 4 weeks in the future"))  # noqa

#         # returning the cleaned data
#         return data


class RenewBookModelForm(forms.ModelForm):
    """ModelForm for renewing a book"""
    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('New renewal date')}
        help_texts = {
            'due_back': _('Enter a date between now and 4 weeks (default 3).')
        }

    def clean_due_back(self):
        """validating the due_back field"""
        data = self.cleaned_data['due_back']

        # check if date is in the future
        if data < date.today():
            raise ValidationError(_("Invalid date - renewal in the past"))

        # check if the date is more than 4 weeks in the future
        if data > (date.today() + timedelta(weeks=4)):
            raise ValidationError(_("Invalid date - renewal more than 4 weeks in the future"))  # noqa

        # returning the cleaned data
        return data
