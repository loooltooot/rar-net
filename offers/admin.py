from django.contrib import admin

from .models import Offer, Photo

# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'status', 'author']
    inlines = [PhotoInline]