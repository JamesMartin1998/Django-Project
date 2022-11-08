from django.contrib import admin
from .models import Movies, Showings, Bookings, Reviews

# admin.site.register(Movies)


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Showings)


admin.site.register(Bookings)

admin.site.register(Reviews)



# Register your models here.
