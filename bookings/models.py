from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Movies(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    day_shown = models.CharField(max_length=50)
    time_shown = models.TimeField()
    description = models.TextField()
    featured_image = CloudinaryField('image')
    run_time = models.IntegerField()
    ticket_price = models.IntegerField()

    def __str__(self):
        return self.title


class Showings(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    seats_remaining = models.IntegerField()

    def __str__(self):
        return f"{self.title} on {self.day_shown} at {self.time_shown}"


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    showing = models.ForeignKey(Showings, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} for {self.title} on {self.day_shown} at {self.time_shown}"




# Create your models here.
