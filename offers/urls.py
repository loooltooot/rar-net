from django.urls import path

from .views import index, CreateOffer, DetailOffer

app_name = 'offers'
urlpatterns = [
    path('', index, name='index'),
    path('offers/new/', CreateOffer.as_view(extra_context={'title': 'Новая заявка'}), name='add_offer'),
    path('offers/<int:pk>/', DetailOffer.as_view(), name='detail_offer'),
]
