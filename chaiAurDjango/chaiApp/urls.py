# URL Configuration for the new app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'), # Home page route with name 'home'
]

