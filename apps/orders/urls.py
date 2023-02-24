from django.urls import path 
from . import views
app_name = 'apps.orders'

urlpatterns = [
    path('add-order/', views.ajax_create_order, name='add_order'),
    path('get-orders/', views.ajax_get_orders, name='get_orders'),
    path('get-order/<str:pk>/', views.ajax_get_order, name='get_order'),
    path('accept-orders/', views.ajax_accept_order, name='accepts_orders'),
    # path('items/', views.ajax_my_cart, name='my_cart_items'),
]