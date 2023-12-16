from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q

from .forms import OfferForm
from .models import Photo, Offer

# Create your views here.

def index(request):
    return render(request, 'offers/index.html', context={'offers': Offer.objects.filter(status='active')})

class CreateOffer(LoginRequiredMixin, generic.CreateView):
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
    else:
        return HttpResponseNotAllowed(['POST'])

class MyOffers(LoginRequiredMixin, generic.ListView):
    model = Offer
    template_name = 'offers/my_offers.html'
    redirect_field_name = ''

    def get_queryset(self):
        return self.request.user.author.all()

@login_required(redirect_field_name='')
def set_selected_responder(request):
    if request.method == 'POST':
        if request.POST is not None:
            offer_pk = request.POST['offer_pk']
            responder_pk = request.POST['responder_pk']

            offer = get_object_or_404(Offer, pk=offer_pk)
            responder = get_object_or_404(get_user_model(), pk=responder_pk)

            if offer.author == request.user:
                offer.selected_responder = responder
                offer.status = 'closed'
                offer.save()
            else:
                return HttpResponseForbidden()

            return redirect('offers:myoffers')
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required(redirect_field_name='')
def reset_selected_responder(request):
    if request.method == 'POST':
        if request.POST is not None:
            offer_pk = request.POST['offer_pk']

            offer = get_object_or_404(Offer, pk=offer_pk)

            if offer.author == request.user:
                offer.selected_responder = None
                offer.status = 'active'
                offer.save()
            else:
                return HttpResponseForbidden()

            return redirect('offers:myoffers')
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required(redirect_field_name='')
def list_user_requests(request):
    user_requests = request.user.responders.all()
    return render(request, 'offers/my_requests.html', context={'requests': user_requests})

def search(request):
    if request.GET is not None:
        query = request.GET['q']
        sort_type = request.GET['sort_type']

        initial_queryset = Offer.objects.filter(status='active')
        sorting_types = {
            'everywhere': initial_queryset,
            'same_country': initial_queryset.filter(author__country=request.user.country),
            'same_city': initial_queryset.filter(author__city=request.user.city),
        }

        sorted_offers = sorting_types.get(sort_type)

        if query is not None:
            sorted_offers = sorted_offers.filter(Q(title__icontains=query) | Q(description__icontains=query))

        return render(request, 'offers/search_page.html', context={'offers': sorted_offers, 'q': query, 'sort_type': sort_type})