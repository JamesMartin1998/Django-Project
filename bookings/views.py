from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views import generic, View
from .models import Movies, Showings, Bookings
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BookingForm

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

        user = request.user
        bookings = Bookings.objects.filter(user=user)
        booking = get_object_or_404(bookings, id=id)

        original_showing = booking.showing.id
        original_tickets = booking.number_of_tickets
        original_seats_remaining = booking.showing.seats_remaining

        form = BookingForm(request.POST, instance=booking)
        
        if form.is_valid():
            form.save()

            new_showing = request.POST.get("showing")
            new_tickets = request.POST.get("number_of_tickets")
            change_in_number_of_tickets_ordered = int(original_tickets) - int(new_tickets)

            print(f"new showing id: {new_showing}")
            print(f"original showing id: {original_showing}")

            if int(new_showing) == int(original_showing):
                # need to update the booking's showing's seats remaining field
                print("hello")
                print(booking.showing.seats_remaining)
                print(change_in_number_of_tickets_ordered)
                booking.showing.seats_remaining = booking.showing.seats_remaining + change_in_number_of_tickets_ordered
                booking.showing.save()
                print(booking.showing.seats_remaining)

            else:
                # need to update seats remaining for original showing and new showing
                print("i am else")
                original_showing_object = get_object_or_404(Showings, id=original_showing)
                print(original_showing_object)
                print(f"Original showing seats remaing: {original_showing_object.seats_remaining}")
                print(f"Original tickets: {original_tickets}")
                original_showing_object.seats_remaining = original_showing_object.seats_remaining + original_tickets
                original_showing_object.save()
                print(f"Original showing seats remaing after save: {original_showing_object.seats_remaining}")


                new_showing_object = get_object_or_404(Showings, id=new_showing)
                print(f"new showing object: {new_showing_object}")
                print(f"new showing object seats remaining before: {new_showing_object.seats_remaining}")
                new_showing_object.seats_remaining = new_showing_object.seats_remaining - int(new_tickets)
                new_showing_object.save()
                print(f"new showing object seats remaining after: {new_showing_object.seats_remaining}")

                


            return redirect('home')