from django.shortcuts import render
from django.shortcuts import HttpResponse

def buy_cart(request):
    if request.is_ajax() and request.method == 'POST':
        products = request.POST['products[]']
        prices = request.POST['prices[]']
        save_order()
        return redirect('mail')
    return HttpResponse(status_code=404)

def save_order():
    print('SAVE ORDER')