from django.urls import path
from . import views
app_name = 'wardens'


urlpatterns=[
    path("register_warden/", views.register_warden, name="register_warden"),
    path('approve_leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('warden_dashboard/', views.warden_dashboard, name='warden_dashboard'),
    path("warden_home/", views.warden_home, name='warden_home'),
    path('warden_login/', views.WardenLoginView.as_view(), name='warden_login'),
    path('warden_logout/', views.WardenLogoutView.as_view(), name='warden_logout'),
]