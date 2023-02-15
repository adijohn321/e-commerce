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
    type = models.CharField(max_length=20,blank=False)
    user = models.ForeignKey(
        MyCustomUser,
        related_name=''
    )
    action = models.CharField(max_length=20,blank=False)
    topic  = models.CharField(max_length=100,blank=False)
    status = models.CharField(max_length=20, blank= False,choices=STATUS_CHOICES, default='new')