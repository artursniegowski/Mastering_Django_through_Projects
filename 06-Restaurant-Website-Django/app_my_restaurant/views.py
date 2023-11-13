from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from .models import Menu
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'app_my_restaurant/index.html')

def about(request):
    return render(request, 'app_my_restaurant/about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # create a new empty form
            form = BookingForm()
            # adding a message for the user
            messages.success(request, 'Booking has been successful!')
    context = {'form':form}
    return render(request, 'app_my_restaurant/book.html', context)

# Add your code here to create new views
def menu(request: HttpRequest) -> HttpResponse:
    menu_data = Menu.objects.all().order_by('name')
    main_data = {'menu':menu_data}
    return render(request, 'app_my_restaurant/menu.html', main_data)

def display_menu_item(request: HttpRequest, pk: int) -> HttpResponse:
    # better way of dealing with it 
    # this will return a 404 instead risde an exception of DoesNotExists!
    # menu_item = get_object_or_404(Menu,pk=pk) 
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    return render(request,'app_my_restaurant/menu_item.html', {"menu_item":menu_item})