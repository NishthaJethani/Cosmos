from django.urls import path
from . import views

urlpatterns=[
    path("register/", views.register_warden, name="register_warden"),
    path('approve-leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('warden_dashboard/', views.warden_dashboard, name='warden_dashboard'),
    path("home/", views.warden_home, name='warden_home'),
    path('login/', views.WardenLoginView.as_view(), name='login'),
    path('logout/', views.WardenLogoutView.as_view(), name='logout'),
]