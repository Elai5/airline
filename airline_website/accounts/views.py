# Create your views here.
# accounts/views.py

from django.shortcuts import render

def login_view(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    return render(request, 'accounts/login.html')