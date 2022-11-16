from django.contrib import admin
from .models import Movies, Showings, Bookings, Reviews


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Showings)
class ShowingsAdmin(admin.ModelAdmin):
    list_display = ('movie', 'location', 'day_shown', 'time_shown',
                             'seats_remaining', 'ticket_price')


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'showing', 'number_of_tickets')


@admin.register(Reviews)
class Reviews(admin.ModelAdmin):
    list_display = ('movie', 'name', 'date_added')
