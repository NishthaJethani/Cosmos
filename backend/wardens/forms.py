from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Warden



class WardenRegistrationForm(UserCreationForm):

    first_name=forms.CharField(max_length=60)
    last_name=forms.CharField(max_length=60)
    phone=forms.CharField(max_length=10)

    class Meta(UserCreationForm.Meta):
        model=Warden
        fields=['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone']

