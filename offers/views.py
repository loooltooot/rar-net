from django.shortcuts import render
from django.views import generic

from locations.models import City

# Create your views here.

def index(request):
    return render(request, 'offers/index.html')