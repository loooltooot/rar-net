from django.urls import path

from .views import (index, CreateOffer, 
    DetailOffer, respond_to_offer, MyOffers, 
    set_selected_responder, reset_selected_responder
)

app_name = 'offers'
urlpatterns = [
    path('', index, name='index'),
    path('offers/new/', CreateOffer.as_view(extra_context={'title': 'Новая заявка'}), name='add_offer'),
    path('offers/<int:pk>/', DetailOffer.as_view(), name='detail_offer'),
    path('offers/<int:pk>/respond/', respond_to_offer, name='respond_offer'),
    path('myoffers/', MyOffers.as_view(extra_context={'title': 'Мои заявки'}), name='myoffers'),
    path('myoffers/select/', set_selected_responder, name='select_responder'),
    path('myoffers/reset/', reset_selected_responder, name='reset_responder'),
]
