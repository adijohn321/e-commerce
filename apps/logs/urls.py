from django.urls import path 
from . import views

app_name = 'apps.logs'

urlpatterns = [
    path('get-notification/', views.ajax_get_notification, name='get_notification'),
    path('get-notifications/', views.ajax_get_notifications, name='get_notifications'),
    path('mark-all/', views.mark_all_as_read, name='mark_all'),
]