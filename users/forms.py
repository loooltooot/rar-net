from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'country', 'city', 'password1', 'password2']
        widgets = {
            'email': forms.TextInput(attrs={'required': ''}),
            'last_name': forms.TextInput(attrs={'required': ''}),
            'first_name': forms.TextInput(attrs={'required': ''}),
            'country': forms.RadioSelect(attrs={'required': ''}),
        }