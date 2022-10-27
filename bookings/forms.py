from django import forms
from .models import Bookings


class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        exclude = ['user', ]
