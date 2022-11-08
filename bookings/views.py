from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views import generic, View
from .models import Movies, Showings, Bookings, Reviews
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BookingForm, ReviewForm
# Line 10/11 imports from https://coderbook.com/@marcus/how-to-restrict-access-with-django-permissions/
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

# allows the user to load the home page
# if they are authenticated, and have made bookgings, they can be seen in a table
class ManageBookings(View):
    def get(self, request):
        # conditional fixes 'AnonymousUser' object is not iterable
        # https://stackoverflow.com/questions/43544366/anonymoususer-object-is-not-iterable-django
        if request.user.is_authenticated:
            user = request.user
            bookings = Bookings.objects.filter(user=user)
            movies = Movies.objects.all()
            spiderman = get_object_or_404(movies, slug='spiderman')

            # code from https://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering
            movies_not_spiderman = Movies.objects.exclude(slug='spiderman').filter()

            context = {
                'bookings': bookings,
                'movies': movies,
                'spiderman': spiderman,
                'movies_not_spiderman': movies_not_spiderman
            }

            return render(request, 'index.html', context)
        else:
            movies = Movies.objects.all()
            spiderman = get_object_or_404(movies, slug='spiderman')

            # code from https://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering
            movies_not_spiderman = Movies.objects.exclude(slug='spiderman').filter()

            context = {
                'movies': movies,
                'spiderman': spiderman,
                'movies_not_spiderman': movies_not_spiderman
            }
            return render(request, 'index.html', context)

""" 
renders all of the movies from the database
"""
def get_movies(request):
    movies = Movies.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies.html', context)

"""
renders all of the movie details to the user
"""
def movie_detail(request, slug):
    if request.method == "GET":
        movies = Movies.objects.all()
        movie = get_object_or_404(movies, slug=slug)
        reviews = movie.reviews.filter().order_by('date_added')
        context = {
            'movie': movie,
            'reviews': reviews,
            'review_form': ReviewForm()
            }
        return render(request, "movie-detail.html", context)

    # Reviews adapts on Comment code from Code Institute's Django Blog Project
    elif request.method == "POST":
        movies = Movies.objects.all()
        movie = get_object_or_404(movies, slug=slug)
        reviews = movie.reviews.filter().order_by('date_added')

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.movie = movie
            review.save()
        else:
            review_form = ReviewForm()

        context = {
            'movie': movie,
            'reviews': reviews,
            'review_form': ReviewForm()
            }

        return render(request, "movie-detail.html", context)

        

# def get_movie_detail(request):
#     movies = Movies.objects.all()


# renders all of the showings for a particular movie
class Shows(View):

    def get(self, request, slug):
        movie = Movies.objects.get(slug=slug)
        showings = Showings.objects.filter(movie=movie)
        context = {
            'movie': movie,
            'showings': showings
        }
        return render(request, "book.html", context)

# allows users to load a form for booking a particular movie showing
# subclasses restrict bookings to only be made by logged in users
# Subclasses from https://coderbook.com/@marcus/how-to-restrict-access-with-django-permissions/
class MakeOrder(LoginRequiredMixin, TemplateView):
    def get(self, request, slug, id):
        movie = Movies.objects.get(slug=slug)
        showing = get_object_or_404(Showings, id=id)

        context = {
            'movie': movie,
            'showing': showing,
        }

        return render(request, "order.html", context)

    def post(self, request, slug, id):
        # allows the user to make a booking
        user = request.user
        movie = Movies.objects.get(slug=slug)
        showing = get_object_or_404(Showings, id=id)
        tickets = request.POST.get("tickets")

        showing.seats_remaining = showing.seats_remaining-int(tickets)

        if int(tickets) == 0:
            messages.error(request, "You can't make a booking with zero tickets. Please increase the number of tickets and try again.")
            return redirect(reverse('order', args=[slug, id]))

        elif int(tickets) < 0:
            messages.error(request, "You can't have a negative number of tickets. Please increase the number of tickets and try again.")
            return redirect(reverse('order', args=[slug, id]))

        elif int(tickets) > 8:
            messages.error(request, "Maximum number of tickets is 8. Please increase the number of tickets and try again.")
            return redirect(reverse('order', args=[slug, id]))

        else:
            # users can only make a booking if they choose a number of tickets that doesn't exceed the remaining number of seats
            if showing.seats_remaining >= 0:
                Bookings.objects.create(user=user, movie=movie, showing=showing, number_of_tickets=tickets)
                showing.save()
                messages.success(request, "Tickets Ordered Successfully!")
                return redirect('home')
            # users receive an error message to inform them that they need to reduce the number of tickets
            # the form is reloaded so users can attempt to book again
            else:
                messages.error(request, "Not enough seats remaining to book tickets. Please reduce your number of tickets and try again.")
                # Code from tutor, John, at Code Institute
                return redirect(reverse('order', args=[slug, id]))

# Allows users to load a template containing a form with their current booking data
# Users can edit their showing and number of tickets
class EditBooking(View):

    def get(self, request, id):
        user = request.user
        movies = Movies.objects.all()
        showings = Showings.objects.all()
        bookings = Bookings.objects.filter(user=user)
        booking = get_object_or_404(bookings, id=id)
        
        
        current_movie = booking.movie
        current_movie_showings = showings.filter(movie=current_movie)

        # Loops through all showings for a particular movie, gets the values from day_shown keys and creates a list. The set then removes duplicate dates.
        def get_current_movie_showings_dates(showings):
            list_of_dates_list = []
            for showing in showings:
                list_of_dates_list.append(showing.day_shown)
            list_of_dates_set = set(list_of_dates_list)
            return list_of_dates_set

        current_movie_showings_dates = get_current_movie_showings_dates(current_movie_showings)

        date_selected = request.POST.get('edit-date')

        form = BookingForm(instance=booking)

        context = {
            'booking': booking,
            'movies': movies,
            'showings': showings,
            'current_movie': current_movie,
            'current_movie_showings': current_movie_showings,
            'current_movie_showings_dates': current_movie_showings_dates,
            'date_selected': date_selected,
            'form': form
        }

        return render(request, 'edit-booking.html', context)

    def post(self, request, id):
        # gets the user and their current booking data
        user = request.user
        bookings = Bookings.objects.filter(user=user)
        booking = get_object_or_404(bookings, id=id)

        original_showing = booking.showing.id
        original_tickets = booking.number_of_tickets
        original_seats_remaining = booking.showing.seats_remaining

        # loads a form with the current booking data
        form = BookingForm(request.POST, instance=booking)
        
        if form.is_valid():
            # gets data about the new booking entered by the user
            new_showing = request.POST.get("showing")
            new_tickets = request.POST.get("number_of_tickets")
            change_in_number_of_tickets_ordered = int(original_tickets) - int(new_tickets)

            print(f"new showing id: {new_showing}")
            print(f"original showing id: {original_showing}")

            if int(new_tickets) == 0:
                messages.error(request, "You can't make a booking with zero tickets. Please increase the number of tickets and try again.")
                return redirect(reverse('edit-booking', args=[id]))

            elif int(new_tickets) < 0:
                messages.error(request, "You can't have a negative number of tickets. Please increase the number of tickets and try again.")
                return redirect(reverse('edit-booking', args=[id]))

            elif int(new_tickets) > 8:
                messages.error(request, "Maximum number of tickets is 8. Please increase the number of tickets and try again.")
                return redirect(reverse('edit-booking', args=[id]))

            else:
                # if the user decides keep the same showing but change the number of tickets
                # updates the number of seats remaining for the showing in the booking
                form.save()

                if int(new_showing) == int(original_showing):
                    print("hello")
                    print(booking.showing.seats_remaining)
                    print(change_in_number_of_tickets_ordered)
                    booking.showing.seats_remaining = booking.showing.seats_remaining + change_in_number_of_tickets_ordered
                    booking.showing.save()
                    print(booking.showing.seats_remaining)
                    messages.success(request, "Your booking has been edited successfully")

                # if the user decides to change the movie showing, with option to change the number of tickets
                # updates the number of seats remaining for the original showing as well as the new showing
                else:
                    # this block updates the number of seats remaining for the original showing
                    print("i am else")
                    original_showing_object = get_object_or_404(Showings, id=original_showing)
                    print(original_showing_object)
                    print(f"Original showing seats remaing: {original_showing_object.seats_remaining}")
                    print(f"Original tickets: {original_tickets}")
                    original_showing_object.seats_remaining = original_showing_object.seats_remaining + original_tickets
                    original_showing_object.save()
                    print(f"Original showing seats remaing after save: {original_showing_object.seats_remaining}")

                    # this block updates the number of seats remaining for the new showing
                    new_showing_object = get_object_or_404(Showings, id=new_showing)
                    print(f"new showing object: {new_showing_object}")
                    print(f"new showing object seats remaining before: {new_showing_object.seats_remaining}")
                    new_showing_object.seats_remaining = new_showing_object.seats_remaining - int(new_tickets)
                    new_showing_object.save()
                    print(f"new showing object seats remaining after: {new_showing_object.seats_remaining}")
                    messages.success(request, "Your booking has been edited successfully")
                return redirect('home')


# Loads the delete booking confirmation page
def delete_booking_page(request, id):
    user = request.user
    bookings = Bookings.objects.filter(user=user)
    booking = get_object_or_404(bookings, id=id)
    context = {'booking': booking}

    return render(request, 'delete-booking.html', context)


# deletes the booking from the database and returns the user to the home page
# corrects the number of seats remaining for the showing
def delete_booking(request, id):
    user = request.user
    bookings = Bookings.objects.filter(user=user)
    booking = get_object_or_404(bookings, id=id)
    showing = booking.showing
    original_seats = booking.showing.seats_remaining
    tickets = booking.number_of_tickets
    booking.delete()
    booking.showing.seats_remaining = original_seats + tickets
    booking.showing.save()
    messages.success(request, "Your booking has been cancelled successfully")
    return redirect('home')


def find_a_cinema(request):
    return render(request, 'find-a-cinema.html')
