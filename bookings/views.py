from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Movies
from django.template import loader

# Create your views here.


class ShowPage():
    def home(request):
        return render(request, 'index.html')

    # def movies(request):
    #     return render(request, 'movies.html')


def get_movies(request):
    movies = Movies.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies.html', context)