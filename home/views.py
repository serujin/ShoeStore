from django.shortcuts import render, redirect
from order_manager.models import Product # TODO: change this to api call

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/signin')
    return render(request, 'home.html', context={'products':Product.objects.all()})