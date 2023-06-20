from django.shortcuts import render, redirect
from .models import Shop,AdsCampaign,Item
from apps.users.models import MyCustomUser
from django.http import (HttpResponseRedirect, JsonResponse)
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic.base import TemplateView

from django.http import HttpResponse
from .forms import *
from apps.cart.models import *
from apps.logs.views import *
from apps.logs.models import *

from django.template.loader import render_to_string
from django.db.models import Q
from PIL import Image
import io

# Create your views here.

def ajax_get_ads(request):
    
    
    if request.user.user_type == "seller":
        _id = request.user.id
        # _id = request.GET.get('user_id')
        user = MyCustomUser.objects.get(id = _id)
        shop = Shop.objects.get(user=user)
        ads = AdsCampaign.objects.filter(shop = shop,).order_by('?')[:10]
    else:

        ads = AdsCampaign.objects.all().order_by('?')[:5]
        


    htmlStr = render_to_string('render_campaign_ads.html', {
        'ads': ads,
    })
    
    return JsonResponse({
        'success': True,
        'htmlStr': htmlStr,
    })



def ajax_get_items(request):
    
    if request.user.user_type == "seller":
        _id = request.user.id
        user = MyCustomUser.objects.get(id = _id)
        shop = Shop.objects.get(user=user)
        items = Item.objects.filter(shop=shop).order_by('?')

    
    else:
        items = Item.objects.all().order_by('?')[:50]
    
    user = MyCustomUser.objects.get(id = request.user.id)

    htmlStr = render_to_string('render_items.html', {
        'items': items,
        'user': user
    })
    
    return JsonResponse({
        'success': True,
        'htmlStr': htmlStr,
    })

def ajax_get_edit_item(request):
    item = Item.objects.get(id = request.GET.get('item_id'))
    htmlStr = render_to_string('render_edit_item.html', {
        'item': item,
    })
    
    return JsonResponse({
        'success': True,
        'htmlStr': htmlStr,
    })

def ajax_get_edit_ad(request):
    item = AdsCampaign.objects.get(id = request.GET.get('item_id'))
    htmlStr = render_to_string('render_edit_ad.html', {
        'item': item,
    })
    
    return JsonResponse({
        'success': True,
        'htmlStr': htmlStr,
    })

def ajax_get_item(request):
    id = request.GET.get('item_id')
    item = Item.objects.get(id=id)
    htmlStr = render_to_string('render_item.html', {
        'item': item
    })
    
    if request.user == item.shop.user:
        htmlStr = render_to_string('render_item_add.html', {
        'item': item
        })
        
    return JsonResponse({
        'success': True,
        'htmlStr': htmlStr,
    })

def ajax_add_item_stock(request):

    if(not request.user.is_authenticated):
        return JsonResponse({'success': False,})
    # import pdb; pdb.set_trace()
    item_id = request.GET.get('item_id')
    try:
        quantity = int(request.GET.get('quantity'))
    except ValueError as ex:
        
        return JsonResponse({'success': False,
        'message':"Please input a number to be added to stock.",
        })
    if quantity<1:
        return JsonResponse({'success': True,
        'message':"Value for quantity cannot be less than or equal to 0.",
    })
    owner = MyCustomUser.objects.get(id=request.user.id)
    item = Item.objects.get(pk=item_id)
    current_stock = item.stock
    
    if not request.user == owner:
        return JsonResponse({'success': False,
        'message':"Failed to add stock.",
    })

    current_stock+= quantity
    item.stock = current_stock
    item.save()
    #send notification to shoppers with wishlists
    items = CartItem.objects.filter(item = item)
    for cart_item in items:
        cart_owner = cart_item.cart.owner
        send_notification(request.user,item,'Added stock to item',cart_owner,'common','')
        
    return JsonResponse({'success': True,
        'message':"Item stock successfully added.",
    })

def ajax_get_items_owner(request):
    serach = request.GET.get('search')

    
    _id = request.user.id
    user = MyCustomUser.objects.get(id = _id)
    shop = Shop.objects.get(user=user)
    items = Item.objects.filter(shop=shop).order_by('name')
    item_id = 1
    if serach:
        items = items.filter(Q(name__icontains=serach)|Q(description__icontains = serach))
    if items:
        item_id = items[0].id


    

    htmlStr = render_to_string('render_items_owner.html', {
        'items': items
    })
    
    return JsonResponse({
        'success': True,
        'htmlStr': htmlStr,
        'item_id':item_id,
    })

def handle_uploaded_image(file):
    img = Image.open(file)
    # Resize the image to your desired dimensions
    img.thumbnail((800, 800))
    # Save the image to a buffer
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG', quality=50)
    # Set the file pointer at the beginning of the buffer
    buffer.seek(0)
    # Return the modified image buffer
    return buffer
 
def ajax_craete_ads(request):
 
    # form = AdsCampaignForm(request.POST, request.FILES)
 
    # if form.is_valid():
    #     # form.save()
    # import pdb;pdb.set_trace()
    
    _id = request.user.id
    user = MyCustomUser.objects.get(id = _id)
    shop = Shop.objects.get(user=user)
    ads_description =request.POST.get('ads_description')
    ads_name = request.POST.get('ads_name')
    ads_image =request.FILES.cleaned_data['file']
    processed_image = handle_uploaded_image(ads_image)
    AdsCampaign.objects.create(
            shop= shop,
            ads_name = ads_name,
            ads_description = ads_description,
            ads_image = processed_image
        )
        
    return JsonResponse({'success': True,})
    
        

 
def ajax_craete_item(request):
    
    _id = request.user.id
    user = MyCustomUser.objects.get(id = _id)
    shop = Shop.objects.get(user=user)
    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    image = request.FILES['itemImage']

    Item.objects.create(
        shop=shop,
        name=name,
        description=description,
        price=price,
        image=image,
    )

    return JsonResponse({'success': True,})

def ajax_update_item(request):
    id = request.POST.get('item_id')
    item = Item.objects.get(id = id)
    item.name = request.POST.get('name')
    item.description = request.POST.get('desc')
    item.price = request.POST.get('price')

    file = request.FILES.get('i-editItemImage')
    if file:
        item.image = file
    item.save()


    
    return JsonResponse({'success': True,'message':'Item Updated.',})

def ajax_update_ad(request):
    id = request.POST.get('item_id')
    item = AdsCampaign.objects.get(id = id)
    item.ads_name = request.POST.get('name')
    item.ads_description = request.POST.get('desc')

    file = request.FILES.get('i-editItemImage')
    if file:
        item.ads_image = file
    item.save()

    print(item)

    
    return JsonResponse({'success': True,'message':'Ads Campaign Updated.',})
 
def success(request):
    return HttpResponse('successfully uplloaded')

class ItemsView(LoginRequiredMixin, TemplateView):
    template_name = 'items.html'
    
    def get_context_data(self, **kwargs):
    
        context = super(ItemsView, self).get_context_data(**kwargs)
        return context

def ajax_item_edit(request):
    shop = Shop.objects.get(user = request.user)
    items = Item.objects.filter(shop = shop)
    item_id = items[0].id

    htmlStr = render_to_string('render_items_view.html', {
        'items': items,
    })
    return JsonResponse({
        'success': True,
        'htmlStr': htmlStr,
        'item_id':item_id,
    })

def ajax_ads_edit(request):
    shop = Shop.objects.get(user = request.user)
    ads = AdsCampaign.objects.filter(shop = shop).order_by('ads_name')
    ad_id = ads[0].id

    htmlStr = render_to_string('render_ads_view.html', {
        'ads': ads,
    })
    return JsonResponse({
        'success': True,
        'htmlStr': htmlStr,
        'item_id':ad_id,
    })


def ajax_delete_item(request):
    item = Item.objects.get(id = request.POST.get('id'))
    if item:
        item.delete()
        return JsonResponse({
        'success': True,
        'message':'Item has been deleted.'
        })
    
    return JsonResponse({
        'success': True,
        'message':'There was an error deleting in item.'
    })
def ajax_delete_ad(request):
    item = AdsCampaign.objects.get(id = request.POST.get('id'))
    if item:
        item.delete()
        return JsonResponse({
        'success': True,
        'message':'Ad Campaign has been deleted.'
        })
    
    return JsonResponse({
        'success': True,
        'message':'There was an error deleting in Ad Campaign.'
    })