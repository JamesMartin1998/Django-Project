from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views import generic, View
from .models import Movies, Showings, Bookings
from django.template import loader
from django.contrib.auth.models import User

# Create your views here.


class ShowPage():
    def home(request):
        return render(request, 'index.html')

    # def sign_up(request):
    #     return render(request, 'signup.html')

    # def movies(request):
    #     return render(request, 'movies.html')


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

        try:
            showing.seats_remaining = showing.seats_remaining-int(tickets)
            if showing.seats_remaining >= 0:
                Bookings.objects.create(user=user, movie=movie, showing=showing, number_of_tickets=tickets)
                showing.save()
                return redirect('home')
            else:
                raise exception(print('Not enough tickets remaining.'))
        except Exception:
            # Code from tutor, John, at Code Institute
            return redirect(reverse('order', args=[slug, id]))
            