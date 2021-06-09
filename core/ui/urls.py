from django.urls import path
from . import views

urlpatterns = [
    path('react', views.react, name='react'),
    path('patientinfo', views.patientinfo, name='patientinfo'),
    path('screen', views.screen, name="screen"),
    path('', views.dashboard, name="dashboard"),
    path('zip', views.zip_analytics, name="zip"),
]
