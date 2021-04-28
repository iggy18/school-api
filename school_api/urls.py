from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from . import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('', views.main_view, name='home'),
    path('people/', views.people_list, name='people'),
    path('campus/', views.campus_list, name='campus'),
]