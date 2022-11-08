from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Movies(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    featured_image = CloudinaryField('image')
    run_time = models.IntegerField()

    def __str__(self):
        return self.title


class Showings(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, default="London")
    day_shown = models.DateField()
    time_shown = models.TimeField()
    seats_remaining = models.IntegerField()
    ticket_price = models.IntegerField()

    def __str__(self):
        return f"{self.movie.title} ({self.location}) on {self.day_shown} at {self.time_shown}"


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    showing = models.ForeignKey(Showings, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} for {self.movie.title} on {self.showing.day_shown} at {self.showing.time_shown}"


# Reviews class code from https://www.youtube.com/watch?v=hZrlh4qU4eQ
class Reviews(models.Model):
    movie = models.ForeignKey(Movies, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.movie.title, self.name)
