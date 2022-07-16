from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , User , PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self , phone , name  ,  email , password):
        if not email:
            raise ValueError('داشتن ایمیل اجباری است')
        if not phone:
            raise ValueError('داشتن شماره تلفن اجباری است')
        if not name:
            raise ValueError('داشتن نام اجباری است')

        user = self.model(
            email = self.normalize_email(email=email),
            name  = name,
            phone = phone
        )
        user.set_password(raw_password=password)
        user.save(using=self._db)    

        return user

    def create_superuser(self , email ,name  , phone , password):

        user = self.create_user(
            email=email,
            name = name,
            phone=phone,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db) 

        return user


class CustomUser(AbstractBaseUser , PermissionsMixin):

    class Meta:
        verbose_name = "مخاطبین سایت"
        verbose_name_plural ="کاربران سایت"


    phone = models.CharField(max_length=11 , unique=True , verbose_name="شماره تلفن")
    name = models.CharField(max_length=40 , verbose_name="نام خانوادگی")
    email = models.EmailField(max_length=50 ,unique=True ,blank=True , null=True , verbose_name="ایمیل")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects= CustomUserManager()

    REQUIRED_FIELDS= ['name','email']
    USERNAME_FIELD= 'phone'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.name

    

