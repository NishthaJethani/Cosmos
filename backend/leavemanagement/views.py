from django.shortcuts import render, redirect, HttpResponse
from .forms import StudentRegistrationForm

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


def home(request):

    context={
        'username':request.user.username
    }
    return render(request, 'home.html', context)