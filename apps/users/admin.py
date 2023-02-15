from django.contrib import admin

# Register your models here.



from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.models import MyCustomUser,UserInformation

@admin.register(MyCustomUser)
class MyCustomUser(AuthUserAdmin):
    fieldsets = (
        (_('Credintials'), {'fields': ( 'email','username', 'password')}),
        (_('User Information'), {'fields': (
            'first_name',
            'last_name',
            'middle_name',
            'extension',
            'user_type',
        )}),
        (_('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions')
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_filedsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password', 'password2')}
        ),
    )

    list_display = ('email','username', 'first_name', 'last_name', 'user_type', 'is_active')
    search_fields = ('email','username', 'first_name', 'last_name')
    ordering = ('email','username',)

@admin.register(UserInformation)
class UserInformation(admin.ModelAdmin):
    fieldsets = (
        (_('User Information'),{ 'fields':('gender', 'phone_number','address')}),
    )
