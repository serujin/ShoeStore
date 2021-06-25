from django.shortcuts import HttpResponse, get_object_or_404
from order_manager.models import Product
import json

# Create your views here.
def get_product_by_name_and_price(request):
    if request.method == 'GET':
        product = get_object_or_404(Product, name=request.GET['name'], price=request.GET['price'])
        return HttpResponse(json.dumps(product_to_dict(product)), content_type="application/json")
    return HttpResponse(status_code=404)

def get_all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = [product_to_dict(product) for product in products]
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(status_code=404)

def product_to_dict(product):
    data = {
        'name': product.name,
        'description': product.description,
        'price': product.price
    }
    return data