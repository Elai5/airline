from django.shortcuts import render

# Create your views here.
# service/views.py

def service_view(request):
    return render(request, 'service/service.html')
