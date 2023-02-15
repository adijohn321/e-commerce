from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(Order)
class Order(admin.ModelAdmin):
    fieldsets = (
        (_('Order'),{'fields':(
            'owner',
            'order_number',
            'status',
        )}),
    )
@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    fieldsets = (
        (_('Order Items'),{'fields':(
            'order',
            'item',
            'quantity',
        )}),
    )