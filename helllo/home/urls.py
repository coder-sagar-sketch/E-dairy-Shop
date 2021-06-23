from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("gallery", views.gallery, name='gallery'),
    path("team", views.team, name='team'),
    path("keepintouch", views.keepintouch, name='keepintouch'),
   
   
    

]