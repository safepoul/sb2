from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , User , PermissionsMixin
# Create your models here.


class CustomUser(AbstractBaseUser , PermissionsMixin):

    phone = models.CharField(max_length=11 , unique=True , verbose_name="شماره تلفن")
    name = models.CharField(max_length=40 , unique=True , verbose_name="نام خانوادگی")
    email = models.EmailField(max_length=50 , verbose_name="ایمیل")
    is_active = True