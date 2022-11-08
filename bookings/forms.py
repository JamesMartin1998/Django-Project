from django import forms
from .models import Bookings, Reviews


class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        exclude = ['user', 'movie', ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('body',)
