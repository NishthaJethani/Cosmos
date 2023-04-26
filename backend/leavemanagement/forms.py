from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Warden

class StudentRegistrationForm(UserCreationForm):

    first_name=forms.CharField(max_length=60)
    last_name=forms.CharField(max_length=60)
    hostel=forms.BooleanField()
    phone=forms.CharField(max_length=10)

    class Meta(UserCreationForm.Meta):
        model=Student
        fields=['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'hostel', 'phone']


class WardenRegistrationForm(UserCreationForm):

    first_name=forms.CharField(max_length=60)
    last_name=forms.CharField(max_length=60)
    phone=forms.CharField(max_length=10)

    class Meta(UserCreationForm.Meta):
        model=Warden
        fields=['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone']

