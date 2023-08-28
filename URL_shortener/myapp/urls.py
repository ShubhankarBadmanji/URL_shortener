from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hello', views.hellow_world),
    path('', views.home_page),
    path('task', views.task_page)
]