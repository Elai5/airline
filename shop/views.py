from django.shortcuts import render

# Create your views here.
# shop/views.py

def shop_view(request):
    return render(request, 'shop/shop.html')
