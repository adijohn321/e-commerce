from django.urls import path 
from . import views

app_name = 'apps.cart'

urlpatterns = [
    path('add-item/', views.add_cart_item, name='add_item'),
    path('items/', views.ajax_my_cart, name='my_cart_items'),
]