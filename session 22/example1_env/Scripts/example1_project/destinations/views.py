from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import all_destinations_list, Destination
import datetime
from django.contrib import messages
from .Forms.DestinationWeather import DestinationWeatherForm


# this is where we receive our requests and 
# accordingly we write the response that should be displayed

# Create your views here.
def destinations(request):
    print("My request: ", request)
    return HttpResponse("My Destinations")

def all_destinations(request):
    print("My request: ", request)
    return HttpResponse(str(all_destinations_list))

def all_destination_HTML(request):
    return render(
        request,
        'allDestinations.html',
        {"destionation_list": all_destinations_list}
    )

# def all_destination_HTML(request):
#     return render(
#         request,
#         'allDestinations.html',
#         {"destionation_list": []}
#     )

def destination(request, id):
    return render(
        request,
        'destination.html',
        {
            "destination": all_destinations_list[id-1]
        }
    )

def filters(request):
    return render(
        request,
        "filters.html",
        {
            "StringFilter" : {
                "lower_upper": "I'm Rhea",
                "wordcount": "I am Rhea Sidana",
                "capfirst": "rhea",
                "list_strings": ["I'm Rhea","Sidana"],
            },
            "IntegerFilter" : {
                "adding": 33,
            },
            "DateTimeFilter" : {
                "dateTimeNow": datetime.datetime.now(),
                "previousDate": datetime.datetime(2024,7,13),
            },
            "ListFilter": {
                "makeListInt": 345,
                "makeListStr": "Rhea Sidana",
            },
            "UnorderedList": ["Rh", ["e", "a", ["Sid", "ana"]]],
            "CustomFilters": {
                "str1": "i am rhea",
                "str2": "sidana",
            },
        }
    )

def all_destinations_destination(request):
    all_destinations = Destination.objects.all()
    # print(all_destinations)
    return render(
        request,
        'all_destinations.html',
        {'destinations': all_destinations,},
    )

def form_view(request):
    if request.method == 'POST':
        form = DestinationWeatherForm(request.POST)
        if form.is_valid():
            messages.success(request, "Admin Secret is valid")
            return redirect("my_destinations")
        else: 
            messages.error(request, "Admin Secret is invalid")
    else:
        form = DestinationWeatherForm()
    return render(
        request=request,
        template_name="formTemplate.html",
        context={
        "form": DestinationWeatherForm
        }
    )

# def form_view(request):
#     return render(
#         request=request,
#         template_name="formTemplate.html",
#         context={
#         "form": DestinationWeatherForm
#         }
#     )
