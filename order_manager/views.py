from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from .models import Order, Product, OrderProduct

def buy_cart(request):
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
    return HttpResponse(status_code=404)

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
        print(product.pk, product.name, product.price)
        order_product = OrderProduct()
        order_product.order = order
        order_product.product = product
        order_product.quantity = quantities[index]
        order_product.save()
