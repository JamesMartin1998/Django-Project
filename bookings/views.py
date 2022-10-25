from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views import generic, View
from .models import Movies, Showings, Bookings
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


class ManageBookings(View):
    def get(self, request):
        # conditional fixes 'AnonymousUser' object is not iterable
        # https://stackoverflow.com/questions/43544366/anonymoususer-object-is-not-iterable-django
        if request.user.is_authenticated:
            user = request.user
            bookings = Bookings.objects.filter(user=user)

            context = {'bookings': bookings}

            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html')


def get_movies(request):
    movies = Movies.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies.html', context)


def movie_detail(request, slug):
    if request.method == "GET":
        movies = Movies.objects.all()
        movie = get_object_or_404(movies, slug=slug)
        context = {'movie': movie}
        return render(request, "movie-detail.html", context)


# def get_movie_detail(request):
#     movies = Movies.objects.all()


class Shows(View):

    def get(self, request, slug):
        movie = Movies.objects.get(slug=slug)
        showings = Showings.objects.filter(movie=movie)
        context = {
            'movie': movie,
            'showings': showings
        }
        return render(request, "book.html", context)


class MakeOrder(View):
    def get(self, request, slug, id):
        movie = Movies.objects.get(slug=slug)
        showing = get_object_or_404(Showings, id=id)

        context = {
            'movie': movie,
            'showing': showing,
        }

        return render(request, "order.html", context)

    def post(self, request, slug, id):
        user = request.user
        movie = Movies.objects.get(slug=slug)
        showing = get_object_or_404(Showings, id=id)
        tickets = request.POST.get("tickets")

        showing.seats_remaining = showing.seats_remaining-int(tickets)
        if showing.seats_remaining >= 0:
            Bookings.objects.create(user=user, movie=movie, showing=showing, number_of_tickets=tickets)
            showing.save()
            messages.success(request, "Tickets Ordered Successfully!")
            return redirect('home')
        else:
            messages.error(request, "Not enough seats remaining to book tickets. Please reduce your number of tickets and try again.")
            # Code from tutor, John, at Code Institute
            return redirect(reverse('order', args=[slug, id]))
            



        # try:
        #     showing.seats_remaining = showing.seats_remaining-int(tickets)
        #     if showing.seats_remaining >= 0:
        #         Bookings.objects.create(user=user, movie=movie, showing=showing, number_of_tickets=tickets)
        #         showing.save()
        #         return redirect('home')
        #     else:
        #         raise exception(print('Not enough tickets remaining.'))
        # except Exception:
        #     # Code from tutor, John, at Code Institute
        #     return redirect(reverse('order', args=[slug, id]))
        