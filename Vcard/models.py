from tkinter import CASCADE
from django.db import models
from jalali_date import datetime2jalali
# Create your models here.
class Vcard(models.Model):

    class Meta:
        verbose_name = "تبلیغات ورقه"
        verbose_name_plural ="تبلیغات ورقه"
    
    title = models.CharField(max_length=100 , verbose_name ='عنوان آگهی')
    idcode=models.CharField(max_length=12 , verbose_name ='کد ورقه مصرفی')
    company=models.CharField(max_length=50 , verbose_name ='نام شرکت')
    color=models.CharField(max_length=50 , verbose_name ='رنگ ورقه')
    width=models.FloatField(verbose_name ='عرض ورقه')
    height=models.FloatField(verbose_name ='طول ورقه')
    higlass = 'HG'
    mdf = 'MF'
    letron = 'LT'
    status = [(higlass,"های گلس"),(mdf,"ام دی اف"),(letron,"لترون")]
    woodType = models.CharField(choices=status , verbose_name ='نوع ورقه' , max_length=2)
    content = models.TextField(verbose_name ='توضیحات')
    image = models.ImageField(upload_to='VcardPhoto/' , verbose_name ='تصویر شاخص' , null=True , blank = True)
    phone =  models.CharField(max_length=11 , verbose_name='تلفن')
    date = models.DateTimeField(verbose_name='زمان شروع' , auto_now_add=True)

    def __str__(self):
        return f'{self.idcode} , {self.company} , {self.color} , {self.woodType}'


    def jalaliDate(self):
        return datetime2jalali(self.date)

