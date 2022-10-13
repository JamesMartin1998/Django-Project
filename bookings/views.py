from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Movies

# Create your views here.

def home(request):
    return render(request, 'index.html')


class MoviesList(generic.ListView):
    model = Movies
    template_name = 'movies.html'