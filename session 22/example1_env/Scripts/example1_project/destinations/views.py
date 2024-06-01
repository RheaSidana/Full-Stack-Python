from django.shortcuts import render
from django.http import HttpResponse
from .models import all_destinations_list

# this is where we receive our requests and 
# accordingly we write the response that should be displayed

# Create your views here.
def destinations(request):
    print("My request: ", request)
    return HttpResponse("My Destinations")

def all_destinations(request):
    print("My request: ", request)
    return HttpResponse(str(all_destinations_list))