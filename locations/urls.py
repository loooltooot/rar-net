from django.urls import path

from .views import get_cities_by_country

app_name = 'locations'
urlpatterns = [
    path('country/<int:pk>/cities/', get_cities_by_country, name='get_cities_by_country'),
]
