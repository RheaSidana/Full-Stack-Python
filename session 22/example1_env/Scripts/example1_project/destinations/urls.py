from django.urls import path
from .views import destinations, all_destinations

urlpatterns = [
    path("e/", destinations, name="my_destinations"),
    path("all/", all_destinations, name="all_destinations"),
]
