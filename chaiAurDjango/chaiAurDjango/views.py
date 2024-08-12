# Importing HttpResponse from django.http module
from django.http import HttpResponse

# Importing render function 
from django.shortcuts import render

# Defining a function named home
def home(request):
    # Returning a HttpResponse object with a string "Home page"
    return render(request, 'website/index.html')

# Defining a function named about
def about(request):
    # Returning a HttpResponse object with a string "About page"
    return HttpResponse("About page")

# Defining a function named contact
def contact(request):
    # Returning a HttpResponse object with a string "Contact page"
    return HttpResponse("Contact page")
