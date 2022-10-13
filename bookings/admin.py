from django.contrib import admin
from .models import Movies, Showings, Bookings

# admin.site.register(Movies)


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'day_shown', 'time_shown')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Showings)


admin.site.register(Bookings)



# Register your models here.
