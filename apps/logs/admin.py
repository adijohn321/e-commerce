from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(Notification)
class Notification(admin.ModelAdmin):
    fieldsets = (
        (_('User Notification'),{ 'fields':('type', 'user','target_user','action','topic','status','message')}),
    )
