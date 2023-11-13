from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from app_booking.models import Booking
from app_booking.forms import BookingForm
from django.core import serializers
from datetime import datetime
from django.db import IntegrityError, DatabaseError, OperationalError
from django.core import serializers
import json

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    """defining the home view"""
    #  not needed as this functionality will be achived with a differetn endpoint!
    # all_bookings = Booking.objects.all().order_by('-date')
    # all_bookings_json = serializers.serialize('json',all_bookings)
    # return render(request, 'app_booking/index.html', {'all_bookings':all_bookings_json})
    return render(request, 'app_booking/index.html')
    
    
def about(request: HttpRequest) -> HttpResponse:
    """defining the about view"""
    return render(request, 'app_booking/about.html')


def book(request: HttpRequest) -> HttpResponse:
    """view for making bookings"""
    # the post request will be handled in a seperate view function 
    # this is only for generating the inputs
    booking_form = BookingForm()
    if request.method == 'POST':
        # to check if it is valid and if not generates error messages in html
        # this wont be used since we are using javaScript to submit the form
        # it is just for protection - you actually cant submit the form from this view
        booking_form = BookingForm(request.POST)
    #     if booking_form.is_valid():
    #         pass
    return render(request, 'app_booking/book.html', {'form': booking_form})


def booking_info(request: HttpRequest) -> HttpResponse:
    """dealing with the POST, GET, DELETE requests for the form"""
    # if POST, retrive the data and validate with the form
    if request.method == 'POST':
        # Load the JSON data from the request body
        # By default, Django can only parse POST requests with application/x-www-form-urlencoded 
        # or multipart/form-data content types. If the content type of the request is different, request.POST will be empty.
        # and we are sending as Content-Type : application/json, 
        # another solution would be to change the fetch request to multipart/form-data or application/x-www-form-urlencoded 
        data = json.loads(request.body.decode('utf-8'))
        form = BookingForm(data)
        if form.is_valid():
            # checkign if booking already exists
            exists = Booking.objects.filter(reservation_slot=form.cleaned_data['reservation_slot']).filter(date=form.cleaned_data['date']).exists()
            if exists:
                return JsonResponse({'status':'error', 'message':'The selected slot for the given date is already taken!'}, status=400)
            else:
                # create the booking
                try:
                    new_booking = Booking.objects.create(
                        name = form.cleaned_data['name'],
                        date = form.cleaned_data['date'],
                        reservation_slot = form.cleaned_data['reservation_slot'],
                    )
                except IntegrityError:
                    return JsonResponse({'status': 'error', 'message': 'Could not create booking due to a database constraint violation.'}, status=400)
                except OperationalError:
                    return JsonResponse({'status': 'error', 'message': 'Database operation failed. Please try again later.'}, status=500)
                except DatabaseError:
                    return JsonResponse({'status': 'error', 'message': 'Error communicating with the database.'}, status=503)
                else:
                    return JsonResponse({'status':'ok'}, status=201)
        else:
            return JsonResponse({'status':'error', 'message':'The form data was not valid!'}, status=400)
    # if a delete request comes
    elif request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        primaryKey = data.get('pk', None)
        
        # if primary key is found we can delete the element fromt he databse
        if primaryKey:
            try:
                booking_to_delete = Booking.objects.get(pk=primaryKey)
                booking_to_delete.delete()
            except Booking.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Cant find a booking with the given primary key.'}, status=400)
            except ValueError:
                return JsonResponse({'status': 'error', 'message': 'The primary key is invalid.'}, status=400)
            except IntegrityError:
                return JsonResponse({'status': 'error', 'message': 'Primary key constraint violation.'}, status=400)
            except (OperationalError, DatabaseError) as e:
                print(f"Error: {e}")
                return JsonResponse({'status': 'error', 'message': 'Error communicating with the database.'}, status=500)  
            else: 
                return JsonResponse({'status':'ok'}, status=200)
        else:
            return JsonResponse({'status':'error', 'message':'The primary key was not found!'}, status=400)
            
    # if GET request we try to retrive the date and if not provided we set to current date
    # and retunr a collection of bookings for that day
    current_date = request.GET.get('date', datetime.today().date())
    bookings_current_date = Booking.objects.filter(date=current_date)
    bookings_current_date = serializers.serialize('json', bookings_current_date)
    bookings_current_date = json.loads(bookings_current_date)
    return JsonResponse({'status':'ok','bookings':bookings_current_date}, status=200, content_type='application/json')


def get_all_bookings(request: HttpRequest) -> HttpResponse:
    """get all bookings"""
    all_bookings = Booking.objects.all().order_by('-date')
    all_bookings_json = serializers.serialize('json',all_bookings)
    all_bookings_json = json.loads(all_bookings_json)
    return JsonResponse({'status':'ok','bookings':all_bookings_json}, status=200, content_type='application/json')
    
    