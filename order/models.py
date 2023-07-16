from django.db import models
from django.contrib.auth import get_user_model
# from phonenumber_field.modelfields import PhoneNumberField

from ice_cream.models import IceCream
# Create your models here.

class Cart(models.Model):
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.ice_cream.name} - {self.quantity}'
    
class Order(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name='Користувач', on_delete=models.CASCADE)
    total = models.PositiveIntegerField(verbose_name='Сума замовлення', default=0)
    first_name = models.CharField(verbose_name='Ім\'я', max_length=255)
    last_name = models.CharField(verbose_name='Прізвище', max_length=255)
    email = models.EmailField(verbose_name='Електронна пошта')
    # phone = PhoneNumberField(verbose_name='Телефон')
    address = models.CharField(verbose_name='Адреса', max_length=255)
    comments = models.TextField(verbose_name='Коментарі', blank=True, null=True)
    created = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)    
    updated = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачено', default=False)

    def __str__(self):  
        return f'Замовлення №{self.id}'