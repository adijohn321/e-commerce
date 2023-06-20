from django.db import models
from Shoppee.models import BaseModel
from apps.users.models import MyCustomUser
from apps.shop.models import Item

from django.utils.translation import gettext_lazy as _

# Create your models here.
class Cart(BaseModel):
    owner = models.OneToOneField(
        MyCustomUser,
        related_name='cart',
        on_delete=models.CASCADE,
        unique=True,
    )
    name = models.CharField(max_length=10,default='Cart')

    def __str__(self):
        return f"{self.owner.full_name}'s cart"


class CartItem(BaseModel):
    cart = models.ForeignKey(
        Cart,
        related_name='cart_items',
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item,
        related_name='cart_item',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.item.name}"

    @property
    def total(self):
        return self.quantity*self.item.price


class Publications(BaseModel):
    title = models.CharField(max_length=100,blank= False,unique=True)
    category = models.CharField(max_length=50,blank= False)
    area = models.CharField(max_length=50,blank = False)
    author = models.CharField(max_length=50,blank = False)
    #keyword = models.CharField(max_length=50,blank = True)
    desc = models.TextField()
    code = models.CharField(max_length=50,blank= False)
    file_link= models.CharField(max_length=20,blank= False)
    cover = models.FileField(upload_to='publications')
    class Meta:
        verbose_name = _('Publication')
        verbose_name_plural = _('Publications')


    def __str__(self):
        return f"{self.title}"

