from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    client     = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # This field is used, so that in case of deleting a product, the total price can be consulted.
    total      = models.DecimalField(max_digits=10, decimal_places=2) 

class Product(models.Model):
    name        = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price       = models.DecimalField(max_digits=10, decimal_places=2)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()