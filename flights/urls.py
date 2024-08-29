# flights/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.plane_schedule_view, name='flights'),
]
