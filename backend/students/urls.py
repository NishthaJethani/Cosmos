from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register_student, name="register_student"),
    path('home/', views.home, name='home'),
    path('login/', views.StudentLoginView.as_view(), name='login'),
    path('logout/', views.StudentLogoutView.as_view(), name='logout'),
]