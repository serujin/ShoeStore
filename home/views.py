from django.shortcuts import render
from product_manager.models import Product
import json

# Create your views here.
def home(request):
    return render(request, 'home.html', context={'products':Product.objects.all()})