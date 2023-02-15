from django.contrib import admin
from .models import Cart,CartItem
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(Cart)
class Cart(admin.ModelAdmin):
    fieldsets = (
        (_('Cart'),{'fields':(
            'owner',
            'name',
        )}),
    )

@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    fieldsets = (
        (_('Cart Item'),{'fields':(
            'cart',
            'item',
            'quantity',
        )}),
    )