from app_catalog.forms import RenewBookModelForm
from datetime import date, timedelta
from django.test import SimpleTestCase
from django.utils.translation import gettext_lazy as _


# class RenewBookFormTest(SimpleTestCase):
#     """Testing the renew book form"""
#     def test_renewal_date_in_past(self):
#         """testing handling dates in the past - validation error"""
#         past_date = date.today() - timedelta(days=1)
#         form = RenewBookForm(data={
#             'renewal_date': past_date
#         })
#         self.assertFalse(form.is_valid())
#         self.assertIn('renewal_date', form.errors)
#         self.assertEqual(
#             form.errors['renewal_date'],
#             [_('Invalid date - renewal in the past')]
#         )

#     def test_renewal_date_more_than_4_weeks_in_future(self):
#         """testing the date more than 4 weeks in future, validation error"""
#         future_date = date.today() + timedelta(weeks=5)
#         form = RenewBookForm(data={
#             'renewal_date': future_date
#         })
#         self.assertFalse(form.is_valid())
#         self.assertIn('renewal_date', form.errors)
#         self.assertEqual(
#             form.errors['renewal_date'],
#             [_('Invalid date - renewal more than 4 weeks in the future')]
#         )

#     def test_valid_renewal_date(self):
#         """testing a valid renewal date"""
#         valid_date = date.today() + timedelta(weeks=2)
#         form = RenewBookForm(data={
#             'renewal_date': valid_date
#         })
#         self.assertTrue(form.is_valid())

class RenewBookFormModelTest(SimpleTestCase):
    """Testing the deu date book form"""
    def test_due_back_date_date_in_past(self):
        """testing handling dates in the past - validation error"""
        past_date = date.today() - timedelta(days=1)
        form = RenewBookModelForm(data={
            'due_back': past_date
        })
        self.assertFalse(form.is_valid())
        self.assertIn('due_back', form.errors)
        self.assertEqual(
            form.errors['due_back'],
            [_('Invalid date - renewal in the past')]
        )

    def test_due_back_date_more_than_4_weeks_in_future(self):
        """testing the date more than 4 weeks in future, validation error"""
        future_date = date.today() + timedelta(weeks=4) + timedelta(days=1)
        form = RenewBookModelForm(data={
            'due_back': future_date
        })
        self.assertFalse(form.is_valid())
        self.assertIn('due_back', form.errors)
        self.assertEqual(
            form.errors['due_back'],
            [_('Invalid date - renewal more than 4 weeks in the future')]
        )

    def test_valid_due_back_date(self):
        """testing a valid due_back"""
        valid_date = date.today() + timedelta(weeks=4)
        form = RenewBookModelForm(data={
            'due_back': valid_date
        })
        self.assertTrue(form.is_valid())
