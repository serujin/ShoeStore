from django.shortcuts import HttpResponse
from order_manager.models import Product
import json

def get_all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = [product_to_dict(product) for product in products]
        if len(data) == 0:
            return HttpResponse(status=204)
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(status_code=404)

def get_product_by_pk(request, pk):
    if request.method == 'GET':
        product = None
        try:
            product = Product.objects.get(pk=pk)
        except:
            return HttpResponse(status=204)
        return HttpResponse(json.dumps(product_to_dict(product)), content_type="application/json")
    return HttpResponse(status_code=404)  

def get_lower_name(name_list):
    product_name = ''
    for word in name_list:
        product_name += word.lower() + ' '
    return product_name[:-1]

def get_capitalize_name(name_list):
    product_name = ''
    for word in name_list:
        product_name += word.capitalize() + ' '
    return product_name[:-1]
    
def get_upper_name(name_list):
    product_name = ''
    for word in name_list:
        product_name += word.upper() + ' '
    return product_name[:-1]

def get_product_by_name(request, name):
    if request.method == 'GET':
        name = name.replace('_', ' ')
        name_list = name.split(' ')
        products_lower = Product.objects.filter(name=get_lower_name(name_list))
        products_capitalize = Product.objects.filter(name=get_capitalize_name(name_list))
        products_upper = Product.objects.filter(name=get_upper_name(name_list))
        data_lower = [product_to_dict(product) for product in products_lower]
        data_capitalize = [product_to_dict(product) for product in products_capitalize]
        data_upper = [product_to_dict(product) for product in products_upper]
        if len(data_lower) > 0:
            return HttpResponse(json.dumps(data_lower), content_type="application/json")
        if len(data_capitalize) > 0:
            return HttpResponse(json.dumps(data_capitalize), content_type="application/json")
        if len(data_upper) > 0:
            return HttpResponse(json.dumps(data_upper), content_type="application/json")
        return HttpResponse(status=204)
    return HttpResponse(status=404)

def get_product_by_price(request, price):
    if request.method == 'GET':
        price = price.replace(',', '.')
        products = Product.objects.filter(price=price)
        data = [product_to_dict(product) for product in products]
        if len(data) == 0:
            return HttpResponse(status=204)
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(status=404)

def format_product_name(name):
    name = name.lower()

def product_to_dict(product):
    data = {
        'name': product.name,
        'description': product.description,
        'price': float(product.price)
    }
    return data