from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postcomment',views.postcomment,name="postcomment"),
    path('',views.queryhome,name='queryhome'),
    path('<str:slug>/',views.querypost,name='querypost'),
    path('postquery',views.postquery,name='postquery'),
    
    
    
    
]
