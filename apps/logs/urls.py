from django.urls import path 
from . import views

app_name = 'apps.logs'

urlpatterns = [
    path('get-notification/', views.ajax_get_notification, name='get_notifications'),
]