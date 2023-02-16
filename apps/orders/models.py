from django.db import models
from Shoppee.models import BaseModel
from apps.users.models import MyCustomUser
from apps.shop.models import Item
from .helpers import *
# Create your models here.




class Order(BaseModel):
    owner = models.ForeignKey(
        MyCustomUser,
        related_name='orders',
        on_delete=models.CASCADE,

    )
    order_number = models.CharField(
        unique=True,
        max_length=100,
        blank=False,
    )
    status = models.CharField(
        max_length=20,
        blank=False,
        choices=STATUS_CHOICES,
        default='pending',
    )

    def __str__(self):
        return self.order_number
    
    @property
    def get_total(self):
        total = 0
        for item in self.order_item.all():
            total+=item.total
        return total
    @property
    def can_approve(self):
        for item in self.order_item.all():
            if item.quantity > item.item.stock:
                return False
        return True

    @property
    def get_shop(self):
        for item in self.order_item.all():
            shop = item.item.shop
        return shop

class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order,
        related_name='order_item',
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item,
        related_name='ordered_item',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.item.name}"

    @property
    def total(self):
        return self.quantity*self.item.price
    @property
    def get_shop(self):
        return self.item.shop