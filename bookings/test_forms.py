from django.test import TestCase
from .forms import BookingForm, ReviewForm

class TestBookingForm(TestCase):

    def test_user_is_required(self):
        form = BookingForm({'user': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('user', form.errors.keys())
        self.assertEqual(form.errors['user'][0], "This field is required.")