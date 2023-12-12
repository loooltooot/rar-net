from django.shortcuts import render
from django.views import generic
from locations.models import City
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import OfferForm
from .models import Photo

# Create your views here.

def index(request):
    return render(request, 'offers/index.html')

class CreateOffer(generic.CreateView, LoginRequiredMixin):
    template_name = 'offers/add_offer.html'
    redirect_field_name = ''
    form_class = OfferForm

    def get_success_url(self):
        return reverse_lazy('offers:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()

        images = form.cleaned_data['imgs']
        for img in images:
            Photo.objects.create(img=img, offer=self.object)

        return HttpResponseRedirect(self.get_success_url())