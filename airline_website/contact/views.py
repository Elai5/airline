from django.shortcuts import render

# Create your views here.
# contact/views.py

def contact_view(request):
    return render(request, 'contact/contact_us.html')


