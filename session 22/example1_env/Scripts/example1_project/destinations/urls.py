from django.urls import path
from .views import *

urlpatterns = [
    path("e/", destinations, name="my_destinations"),
    path("all/", all_destinations, name="all_destinations"),
    path("all_destinations/", all_destinations_destination, name="all_destinations_destination"),
    path("all_HTML/", all_destination_HTML, name="all_destinations_in_HTML"),
    path("all_HTML/<int:id>", destination, name="destination"),
    path("form/", form_view, name="form"),

    # not related to destinations but related to Template Filters
    path("filters/", filters, name="filters"),
]
