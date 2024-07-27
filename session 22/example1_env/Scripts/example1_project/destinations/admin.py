from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Destination)
admin.site.register(DestiantionWeather)