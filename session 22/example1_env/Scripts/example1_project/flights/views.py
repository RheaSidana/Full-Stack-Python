# Create your views here.
from django.http import HttpResponse
from .models import flights

def all_flights(req):
    print("Req: ", req)
    return HttpResponse(str(flights))