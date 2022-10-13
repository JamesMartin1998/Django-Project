from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowPage.home, name='home'),
    path('movies/', views.ShowPage.movies, name='movies'),
]