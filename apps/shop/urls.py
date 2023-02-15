from django.urls import path 
from . import views

app_name = 'apps.shop'

urlpatterns = [
    path('ajax-ads/', views.ajax_get_ads, name='ads'),
    path('ajax-items/', views.ajax_get_items, name='items'),
    path('ajax-item-edit/', views.ajax_get_edit_item, name='edit_item'),
    path('ajax-item-ads/', views.ajax_get_edit_ad, name='edit_ads'),
    path('ajax-item-update/', views.ajax_update_item, name='update_item'),
    path('ajax-item-delete/', views.ajax_delete_item, name='delete_item'),
    path('ajax-ad-delete/', views.ajax_delete_ad, name='delete_ad'),
    path('ajax-ad-update/', views.ajax_update_ad, name='update_ad'),
    path('ajax-items-owner/', views.ajax_get_items_owner, name='items_owner'),
    path('ajax-ads-owner/', views.ajax_get_items_owner, name='ads_owner'),
    path('ajax-create-ads/', views.ajax_craete_ads, name='create_ads'),
    path('ajax-create-item/', views.ajax_craete_item, name='create_item'),
    path('ajax-add-item-stock/', views.ajax_add_item_stock, name='add_item_stock'),
    path('items/', views.ItemsView.as_view(), name='items_view'),
    path('edit-items/', views.ajax_item_edit, name='edit_items'),
    path('edit-ads/', views.ajax_ads_edit, name='ads_items'),
    path('item/', views.ajax_get_item, name='item'),
]