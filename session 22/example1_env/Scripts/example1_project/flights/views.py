# Create your views here.
from django.http import Http404
# from django.http import HttpResponse
from django.shortcuts import render
from .models import flights

def all_flights(req):
    print("Req: ", req)
    return render(
        req, 
        'flights.html', 
        {'flights': flights}
    )

def flight(req, id):
    print("Req: ", req)
    print("id: ", id)
    try:
        flight = flights[id]
    except IndexError:
        raise Http404("Flight does not exist")
    return render(
        req, 
        'flight.html', 
        {'flight': flight}
    )