from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowPage.home, name='home'),
    path('movies/', views.get_movies, name='movies'),
    path('movies/<slug:slug>/', views.movie_detail, name='movie-detail'),
    path('movies/<slug:slug>/book/', views.Book.as_view(), name='book')
]