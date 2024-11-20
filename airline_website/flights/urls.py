# flights/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.plane_schedule_view, name='flights'),  # Matches flights/
    path('log/', views.log_view, name='log'),  # Matches flights/log-in/
]
