from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from .models import Movies, Showings
from django.template import loader

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


class Book(View):

    def get(self, request, slug):
        movie = Movies.objects.get(slug=slug)
        showings = Showings.objects.filter(movie=movie)
        context = {
            'showings': showings
        }
        return render(request, "book.html", context)