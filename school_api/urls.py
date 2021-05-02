from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from . import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('api/v1/', views.main_view, name='home'),
    path('api/v1/people/', views.PeopleList.as_view(), name='people'),
    path('api/v1/campus/', views.campus_list, name='campus'),
    path('api/v1/class/', views.class_list, name='class'),
]