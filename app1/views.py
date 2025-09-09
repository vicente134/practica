from django.shortcuts import render
from django.urls import path
from .import views
# Create your views here.
urlpatterns = [
path('v1/', views.vista1, name='app1-v1'),
path('v2', views.vista2, name='app2-v2'),
]