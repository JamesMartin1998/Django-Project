from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Movies

# Create your views here.


class ShowPage():
    def home(request):
        return render(request, 'index.html')

    def movies(request):
        return render(request, 'movies.html')






class MoviesList(generic.ListView):
    model = Movies
    template_name = 'movies.html'