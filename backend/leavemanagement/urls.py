from django.urls import path
from . import views

urlpatterns=[
    path("student/register", views.register_student, name="register_student"),
    path("home", views.home, name='home'),
]