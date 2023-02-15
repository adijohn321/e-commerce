from django.shortcuts import render
import random
import string


# Create your views here.


from django.urls import reverse_lazy
from django.http import (HttpResponseRedirect, JsonResponse)
from django.views.generic.base import TemplateView

from apps.users.models import MyCustomUser
from apps.shop.models import Item
from apps.cart.models import *
from .models import *
from django.template.loader import render_to_string
from apps.shop.models import *
from django.db.models import Q



def ajax_create_order(request):


    items = request.POST.getlist('items')
    quantities = request.POST.getlist('quantities')
    order_number = get_random_string(20)
    Order.objects.create(owner = request.user,
        order_number = order_number,
        status='pending'
    )
    order = Order.objects.get(order_number = order_number)
    for i in range(0, len(items)):
        my_item = Item.objects.get(id = items[i])
        add_item_order(my_item,order,quantities[i])
        remove_cart_item(my_item,request.user)
        
    return JsonResponse({
        'success':True,
    })

def add_item_order(item,order,quantity):
    OrderItem.objects.create(
        order= order,
        item=item,
        quantity=quantity,
    )

def remove_cart_item(item, user):
    cart = Cart.objects.get(owner = user)
    my_item = CartItem.objects.get(
        cart=cart,
        item = item,
    )
    my_item.delete()


def get_random_string(length):

    import datetime 

    dt = datetime.datetime.now()
    seq = int(dt.strftime("%Y%m%d%H%M%S"))
    chars = string.ascii_lowercase
    result_str = ''.join(random.choice(chars) for i in range(length))
    return str(seq)+result_str

def ajax_get_orders(request):
    status = request.GET.get('status')
    order = Order.objects.filter(status = status)
    if status == 'preparing':
        order = Order.objects.filter( Q(status = status) | Q(status = 'request_cancel'))

    items = Item.objects.all()
    htmlStr = render_to_string('render_orders.html', {
        'orders':order,
        'items':items,
        'status':status,
    })

    if request.user.user_type == 'shopper':
        order = Order.objects.filter( owner = request.user, status = status)
        if status == 'preparing':
            order = Order.objects.filter(Q( owner = request.user) &(Q(status = status)|Q(status = 'request_cancel')))
        htmlStr = render_to_string('render_orders_shopper.html', {
        'orders':order,
        'status':status,
        })

    
    return JsonResponse({
        'success': True,
        'htmlStr': htmlStr,
    })

def ajax_accept_order(request):
    status = request.POST.get('status')
    order = Order.objects.get(order_number = request.POST.get('order_number'))
    current_status = order.status
    if status == 'request_cancel' and current_status == 'otw':
        return JsonResponse({
        'success': True,
        'message':'Operation failed the order already out for delivery.',
        })
    if current_status == 'canceled':
        return JsonResponse({
        'success': True,
        'message':'Operation failed the order was canceled by the customer.',
        })
        
    order.status = status
    order.save()

    items = OrderItem.objects.filter(order = order)
    
    if current_status == 'request_cancel' and status == 'canceled':
        for item in items:
            update_item_stock(item.quantity*(-1),item.item.id)
    if status == 'preparing':
        for item in items:
            update_item_stock(item.quantity,item.item.id)

    
    return JsonResponse({
        'success': True,
        'message':'Operation was successful.',
    })

def update_item_stock(quantity, item_id):
    item = Item.objects.get(id = item_id)
    stock =  item.stock
    item.stock = (stock - (quantity))
    item.save()


