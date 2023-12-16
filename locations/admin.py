from django.contrib import admin

from .models import Country, City

# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['name__icontains']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name__icontains']