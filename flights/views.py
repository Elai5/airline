from django.shortcuts import render

# Create your views here.
# flights/views.py

def plane_schedule_view(request):
    return render(request, 'flights/plane_schedule.html')
