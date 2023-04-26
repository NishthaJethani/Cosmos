from django.urls import path
from . import views

urlpatterns=[
    path("warden/register", views.register_warden, name="register_warden"),

    path("home/", views.home, name='home'),
    path('login/', views.WardenLoginView.as_view(), name='login'),
    path('logout/', views.StudentLogoutView.as_view(), name='logout'),
]