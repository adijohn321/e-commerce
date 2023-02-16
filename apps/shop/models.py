from django.db import models

# Create your models here.

from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from Shoppee.models import BaseModel
from apps.users. models import MyCustomUser

class Shop(BaseModel):
    
    user = models.OneToOneField(
        MyCustomUser,
        related_name='shop',
        on_delete=models.CASCADE,
    )
    shop_name = models.CharField(max_length=20,blank = False, unique = True)
    
    def __str__(self):
        return f" {self.shop_name} - {self.user.full_name}"



class AdsCampaign(BaseModel):
    shop = models.ForeignKey(
        Shop,
        related_name='shop_ads',
        on_delete=models.CASCADE,
    )
    ads_description = models.CharField(max_length= 100)
    ads_name = models.CharField(max_length= 50, unique = True,blank=False)
    
    ads_image = models.ImageField(default='ad1.jfif', upload_to='Ads_Images')

    def __str__(self):
        return f"{self.shop} - {self.ads_name}"


class Item(BaseModel):
    shop = models.ForeignKey(
        Shop,
        related_name='items',
        on_delete=models.CASCADE,
    )
    name= models.CharField(max_length=50,blank=False)
    description= models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, default=0,decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(default='item1',upload_to='Items')

    def __str__(self):
        return f"{self.name}"
    
    @property
    def get_short_desc(self):
        return f"{self.description[0:30]}..."
    
    @property
    def get_total_ordered(self):
        items = self.ordered_item.all()
        total = 0
        for item in items:
            if item.order.status == 'pending':
                total+= item.quantity
        return total
    
    
    @property
    def get_total_in_cart(self):
        items = self.cart_item.all()
        total = 0
        for item in items:
            total+= item.quantity
        return total
    @property
    def get_item_rating(self):
        rate = 0
        if not self.item_rating.all():
            return 0
        for item_rating in self.item_rating.all():
            rate += item_rating.rate
        return rate/len(self.item_rating.all())
    
class ItemRating(BaseModel):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='item_rating',
    )
    rate = models.FloatField(blank=False)
    user = models.ForeignKey(
        MyCustomUser,
        blank=False,
        on_delete=models.CASCADE,
    )
    comment = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return f"{self.user.full_name} rated {self.item} {self.rate}"
