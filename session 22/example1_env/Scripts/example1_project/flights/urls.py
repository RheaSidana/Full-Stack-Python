from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_flights, name="all_flights"),
    path('<int:id>/', views.flight, name="flight"),
]
