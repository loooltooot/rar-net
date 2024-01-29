from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.views import generic
from django.urls import reverse_lazy
from offers.models import Offer

from .forms import LoginForm, RegisterForm

# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('offers:index')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return redirect('offers:index')
            else:
                return render(request, 'offers/index.html', {'error': 'Неправильный пароль или логин', 'offers': Offer.objects.filter(status='active')})
        
    return redirect('offers:index')

class RegisterUser(generic.CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        form.save()
        new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, new_user)
        return redirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('offers:index')