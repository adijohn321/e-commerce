from django.shortcuts import render
from .models import *
from django.http import (HttpResponseRedirect, JsonResponse)
from django.template.loader import render_to_string
from apps.users.models import MyCustomUser
from apps.shop.models import *

# Create your views here.

def ajax_get_notification(request):
    new_notification = Notification.objects.filter(target_user = request.user,status = 'new')
    return JsonResponse({
        'success':True,
        'notifications':len(new_notification),
    })

def send_notification(user,topic,action,target_user,type,message):
    Notification.objects.create(
        user = user,
        action= action,
        target_user = target_user,
        type = type,
        message = message,
        topic = topic
    )
