from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createconfig/', views.CreateConfig, name='createconfig'),
    path('buildconfig/', views.BuildConfig, name='buildconfig'),

    re_path(r'^.*\.*', views.pages, name='pages'),
    

]
