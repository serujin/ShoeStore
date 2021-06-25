from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from .models import Order, Cart
from product_api.models import Product

def buy_cart(request):
    if not request.user.is_authenticated:
        return redirect('/signin')
    if request.is_ajax() and request.method == 'POST':
        products = request.POST.getlist('products[]')
        quantities = request.POST.getlist('quantities[]')
        prices = request.POST.getlist('prices[]')
        total = request.POST['total']
        request.session['products'] = products 
        request.session['quantities'] = quantities
        request.session['prices'] = prices
        request.session['total'] = total
        save_order(request)
        return redirect('/email')
    return HttpResponse(status=404)

def save_order(request):
    products = request.session['products']
    quantities = request.session['quantities']
    prices = request.session['prices']
    total = request.session['total']
    order = Order()
    order.client = request.user
    order.total = total[:-1]
    order.save()
    for index in range(len(products)):
        product = Product.objects.get(name=products[index], price=prices[index][:-1])
        cart = Cart()
        cart.order = order
        cart.product = product
        cart.quantity = quantities[index]
        cart.save()
