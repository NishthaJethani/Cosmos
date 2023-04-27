from django.shortcuts import render, redirect, get_object_or_404
from .forms import WardenRegistrationForm
from .backends import WardenBackend
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from leavemanagement.models import LeaveApplication
from django.urls import reverse_lazy

# Create your views here.

def register_warden(request):
    if request.method=='POST':
        form=WardenRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warden_dashboard')
        
    else:
            form=WardenRegistrationForm()
    return render(request, 'register_warden.html', {'form': form})

def warden_home(request):

    context={
        'username':request.user.username
    }
    return render(request, 'warden_home.html', context)

'''class StudentLoginView(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True
    success_url='home/'
'''

class WardenLoginView(LoginView):
    authentication_backend = WardenBackend
    template_name = 'warden_login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('warden_dashboard')


class WardenLogoutView(LogoutView):
    template_name='warden_logout.html'



'''def approve_leave(request):
    if not request.user.warden:
        # If the current user is not a warden, redirect to home
        return redirect('home')
    if request.method == 'POST':
        leave_application_id = request.POST.get('leave_application_id')
        leave_application = LeaveApplication.objects.get(id=leave_application_id)
        leave_application.status = 'A'
        leave_application.save()
        return redirect('approve_leave')
    else:
        pending_leave_applications = LeaveApplication.objects.filter(status='P')
        context = {
            'pending_leave_applications': pending_leave_applications
        }
        return render(request, 'approve_leave.html', context)
'''

def approve_leave(request, leave_id):
    leave_application = get_object_or_404(LeaveApplication, id=leave_id)
    leave_application.status = 'A'
    leave_application.save()
    messages.success(request, 'Leave application approved.')
    return redirect('warden_dashboard')


def warden_dashboard(request):

    pending_leaves = LeaveApplication.objects.filter(status='P')
    return render(request, 'warden_dashboard.html', {'pending_leaves': pending_leaves})

