from django.contrib import admin
from .models import Product, Order, OrderProduct

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)