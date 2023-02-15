from django.db import models
from Shoppee.models import BaseModel
from apps.users.models import MyCustomUser
from apps.shop.models import Item

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