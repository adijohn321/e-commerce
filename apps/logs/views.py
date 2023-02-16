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

def ajax_get_notifications(request):
    notifications = Notification.objects.filter(target_user = request.user).order_by('created_at').reverse()

    htmlStr = render_to_string(
        'render_notifications.html', {
        'notifications': notifications,
    }
    )
    return JsonResponse({
        'success':True,
        'htmlStr':htmlStr,
    })

def mark_all_as_read(request):
    Notification.objects.filter(target_user = request.user).update(status = 'read')
    return JsonResponse({
        'success':True,
        'message':'Marked all as read.',
    })
