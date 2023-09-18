from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ansible'

urlpatterns = [
    path('', views.index, name=''),
    path('push_file', views.push_file, name='push_file')
]   