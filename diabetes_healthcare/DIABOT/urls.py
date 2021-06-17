from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('homepage/', views.homepage, name='homepage'),
    path('userDashboard/', views.userDashboard, name='userDashboard'),
    path('medicalDashboard/', views.medicalDashboard, name='medicalDashboard'),
]
