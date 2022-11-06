from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManageBookings.as_view(), name='home'),
    path('movies/', views.get_movies, name='movies'),
    path('movies/<slug:slug>/', views.movie_detail, name='movie-detail'),
    path('movies/<slug:slug>/shows/', views.Shows.as_view(), name='shows'),
    path('movies/<slug:slug>/shows/<int:id>/', views.MakeOrder.as_view(), name='order'),
    path('edit-booking/<int:id>/', views.EditBooking.as_view(), name='edit-booking'),
    path('delete-booking/<int:id>/', views.delete_booking_page, name='delete-booking'),
    path('delete/<int:id>/', views.delete_booking, name='delete'),
    path('find-a-cinema/', views.find_a_cinema, name='find-a-cinema')
]