from django.shortcuts import render, redirect
from apps.users.models import MyCustomUser
from apps.shop.models import *
from django.http import (HttpResponseRedirect, JsonResponse)
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import *
from django.template.loader import render_to_string

# Create your views here.


def add_cart_item(request):
    if(not request.user.is_authenticated):
        return JsonResponse({'success': False,})
    # import pdb; pdb.set_trace()
    _id = request.user.id
    item_id = request.GET.get('item_id')
    quantity = request.GET.get('quantity')
    owner = MyCustomUser.objects.get(id=_id)
    cart = Cart.objects.get(owner = owner)
    item = Item.objects.get(pk=item_id)
    if CartItem.objects.filter(cart = cart,
        item = item,):
        return JsonResponse({'success': True,
            'message':"This item is already in the cart.",
        })
    CartItem.objects.create(
        cart = cart,
        item = item,
        quantity= quantity,
    )
    return JsonResponse({'success': True,
        'message':"Item successfully added to your cart.",
    })


def ajax_my_cart(request):
    cart = Cart.objects.get(owner = request.user)
    items = CartItem.objects.filter(cart = cart)

    htmlStr = render_to_string('render_cart.html', {
        'items': items,
    })
    return JsonResponse({
        'success': True,
        'htmlStr': htmlStr,
    })
