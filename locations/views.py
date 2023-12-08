from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core import serializers

from .models import City

# Create your views here.

def get_cities_by_country(request, pk):
    cities = City.objects.filter(country__id=pk)

    if len(cities) == 0:
        raise Http404

    data = serializers.serialize('json', cities)

    return HttpResponse(data, content_type='application/json')