from django.urls import path
from .views import *

urlpatterns = [
    path("form-user-registration/", user_registration, name="user_registration"),
]