from django.urls import path 
from . import views


app_name = 'apps.users'

urlpatterns = [
    path('login/',views.loginUser, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('ajax_register/', views.ajax_register, name='register'),
]

