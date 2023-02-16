from django.db import models
from apps.cart.models import *
from apps.orders.models import *
from apps.shop.models import *
from apps.users.models import *
from Shoppee.models import BaseModel
from django.utils.translation import gettext_lazy as _
# Create your models here.
STATUS_CHOICES = (
    ('new','NEW'),
    ('read','READ'),
)
NOTIFICATION_TYPE_CHOICES = (
    ('important','IMPORTANT'),
    ('common','COMMON'),
    ('broadcast','BROADCAST'),
)

class Notification(BaseModel):
    type = models.CharField(max_length=20,blank=False, choices=NOTIFICATION_TYPE_CHOICES)
    user = models.ForeignKey(
        MyCustomUser,
        related_name='notifications',
        on_delete = models.CASCADE
    )
    target_user = models.ForeignKey(
        MyCustomUser,
        related_name='my_notifications',
        on_delete = models.CASCADE
    )
    action = models.CharField(max_length=100,blank=False)
    topic  = models.CharField(max_length=100,blank=False)
    status = models.CharField(max_length=20, blank= False,choices=STATUS_CHOICES, default='new')
    message = models.CharField(max_length=200 , blank=True, null=True)

    def __str__(self):
        return f"{self.user} {self.action} {self.topic}"

    @property
    def get_new(self):
        return len(self.filter(status = 'new'))