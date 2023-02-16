from django.contrib import admin

from django.utils.translation import gettext_lazy as _

from .models import Shop,AdsCampaign, Item,ItemRating

# Register your models here.


@admin.register(Shop)
class Shop(admin.ModelAdmin):
    fieldsets = (
        (_('Shop Information'),{ 'fields':('user', 'shop_name')}),
    )
    
@admin.register(AdsCampaign)
class AdsCampaign(admin.ModelAdmin):
    fieldsets = (
        (_('Shop Information'),{ 'fields':('shop','ads_description','ads_name','ads_image',)}),
        (_('Permissions'), {'fields': (
            'is_active',)
        }),
    )

@admin.register(Item)
class Item(admin.ModelAdmin):
    fieldsets = (
        (_('Item Information'),{'fields':('shop','name','description','price','stock','image')}),
        (_('Permissions'), {'fields': (
            'is_active',)
        }),
    )


@admin.register(ItemRating)
class ItemRating(admin.ModelAdmin):
    fieldsets = (
        (_('Item Rating'),{'fields':('item','rate','user','comment')}),
        (_('Permissions'), {'fields': (
            'is_active',)
        }),
    )