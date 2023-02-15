from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .helpers import optional, USER_TYPE_CHOICES,GENDER_CHOICES
from django.utils.translation import gettext_lazy as _
from Shoppee.managers import CustomUserManager
from django.core.validators import RegexValidator
from Shoppee.models import BaseModel


class MyCustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, blank=False)
    middle_name = models.CharField(max_length=50, **optional)
    last_name = models.CharField(max_length=50, blank=False)
    extension = models.CharField(max_length=50,**optional)
    email = models.EmailField(unique=True)
    username= models.CharField(_('Username'),max_length=100,blank=False,unique= True)
    user_type = models.CharField(max_length=10,choices=USER_TYPE_CHOICES,default='shopper')

    
    is_superadmin = models.BooleanField(_('is_superadmin'), default=False)
    is_active = models.BooleanField(_('is_active'), default=False)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS =[
        'first_name',
        'last_name',
        'email',

    ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.username}({self.user_type})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name if self.middle_name else ''} {self.last_name} {self.extension if self.extension else ''}"

class UserInformation(BaseModel):
    user = models.OneToOneField(
        MyCustomUser,
        related_name='user_information',
        on_delete=models.CASCADE,
        unique=True,
    )
    mobile_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Mobile number format must be: '+639999999999'.")
    phone_number = models.CharField(validators=[mobile_regex], max_length=20,unique=True)
    gender = models.CharField(max_length=20,**optional,choices=GENDER_CHOICES)
    address = models.CharField(max_length=200,**optional)
    #address-
    #contact-
    #telephone
    #facebook
    #website
    #
    #

    
    def __str__(self):
        return f"{self.user.full_name}"


    @property
    def get_user_id(self):
        return self.user.id


