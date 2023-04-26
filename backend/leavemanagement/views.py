from django.shortcuts import render, redirect, HttpResponse
from .forms import StudentRegistrationForm, WardenRegistrationForm

from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
def register_student(request):
    if request.method=='POST':
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
            form=StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})

def register_warden(request):
    if request.method=='POST':
        form=WardenRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
            form=WardenRegistrationForm()
    return render(request, 'register_warden.html', {'form': form})

def home(request):

    context={
        'username':request.user.username
    }
    return render(request, 'home.html', context)

class StudentLoginView(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True
    success_url='home/'

class StudentLogoutView(LogoutView):
    template_name='logout.html'