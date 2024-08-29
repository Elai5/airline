from django.shortcuts import render

# Create your views here.
# about/views.py

def about_view(request):
    return render(request, 'about/about.html')
