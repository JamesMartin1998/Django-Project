from django.test import TestCase
from .forms import BookingForm, ReviewForm
from .models import Bookings, Reviews


class TestBookingForm(TestCase):

    def test_correct_model(self):
        form = BookingForm()
        self.assertEqual(form.Meta.model, Bookings)

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.exclude, ['user', 'movie'])


class TestReviewForm(TestCase):

    def test_correct_model(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.model, Reviews)

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ('body',))