from django.shortcuts import render, redirect, HttpResponse
from .forms import StudentRegistrationForm
from .backends import StudentBackend
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

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




'''class StudentLoginView(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True
    success_url='home/'
'''

class StudentLoginView(LoginView):
    authentication_backend = StudentBackend
    template_name = 'login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')




class StudentLogoutView(LogoutView):
    template_name='logout.html'

#@login_required
def home(request):

    context={
        'username':request.user.username
    }
    return render(request, 'home.html', context)
