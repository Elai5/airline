# service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_view, name='service'),
]