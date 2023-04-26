from django.shortcuts import render, redirect, HttpResponse
from .forms import StudentRegistrationForm
from .backends import StudentBackend
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from leavemanagement.models import LeaveApplication
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
    template_name = 'student_login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('dashboard')




class StudentLogoutView(LogoutView):
    template_name='student_logout.html'
    



def apply_leave(request):
    if request.method == 'POST':
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        reason=request.POST['reason']
        student=request.user

        leave_application=LeaveApplication(
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            student=student,
        )
        leave_application.save()
        messages.success(request, 'Leave application submitted successfully.')
        return redirect('dashboard')
    else:
        return render(request, 'apply_leave.html')


def student_dashboard(request):
    leave_applications = request.user.leave_applications.all()
    return render(request, 'student_dashboard.html', {'leave_applications': leave_applications})




#@login_required
def student_home(request):

    context={
        'username':request.user.username
    }
    return render(request, 'student_home.html', context)
