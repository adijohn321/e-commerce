"""Shoppee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls',namespace='users')),
    path('orders/', include('apps.orders.urls',namespace='orders')),
    path('shop/', include('apps.shop.urls',namespace='shop')),
    path('cart/', include('apps.cart.urls',namespace='cart')),
    path('logs/', include('apps.logs.urls',namespace='logs')),
    path('login', views.LoginView.as_view(),name='login'),
    path('', views.home.as_view(),name='home'),
    path('profile', views.Profile.as_view(),name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
