from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from locations.models import City
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import F

from .forms import OfferForm
from .models import Photo, Offer

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

class DetailOffer(generic.DetailView):
    model = Offer
    template_name = 'offers/detail_offer.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailOffer, self).get_context_data(*args, **kwargs)
        context['title'] = context['offer'].title
        return context

@login_required(redirect_field_name='')
def respond_to_offer(request, pk):
    if request.method == 'GET':
        offer = get_object_or_404(Offer, pk=pk)
        offer.responders.add(request.user)
        offer.save()

        return redirect('offers:index')