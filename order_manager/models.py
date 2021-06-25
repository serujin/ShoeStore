from django.db import models
from django.contrib.auth.models import User
from product_api.models import Product

class Order(models.Model):
    client     = models.ForeignKey(User, on_delete=models.CASCADE)
    products   = models.ManyToManyField(Product, through='Cart')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # This field is used, so that in case of deleting a product, the total price can be consulted.
    total      = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.client.username + ' ' + self.created_at.strftime('%d-%m-%Y %H:%M ')

class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()