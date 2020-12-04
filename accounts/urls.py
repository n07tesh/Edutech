from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    #path('',views.home,name='home'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),


 
]