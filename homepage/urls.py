from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('createconfig/', views.CreateConfigView.as_view(), name='createconfig'),
    path('buildconfig/', views.BuildConfigView.as_view(), name='buildconfig'),
    path('sel1/', views.SelclassView.as_view(), name='sel1'),
    path('about/', views.AboutView.as_view(), name='about')
]