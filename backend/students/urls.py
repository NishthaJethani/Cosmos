from django.urls import path
from . import views
app_name = 'students'

urlpatterns=[
    path('register_student/', views.register_student, name="register_student"),
    path('student_home/', views.student_home, name='student_home'),
    path('student_login/', views.StudentLoginView.as_view(), name='student_login'),
    path('student_logout/', views.StudentLogoutView.as_view(), name='student_logout'),
    path('apply_leave/', views.apply_leave, name='apply_leave'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
]