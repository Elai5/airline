from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def index(request):
    return render(request, 'home/index.html')
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('home') 