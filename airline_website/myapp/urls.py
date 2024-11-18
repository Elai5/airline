from django.urls import path
from . import views

urlpatterns = [
    path('app1/', views.app1_view, name='app1_home'),
    # Add more routes for app1 if needed
]
