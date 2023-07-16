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
    STATUC_CHOICES =(
        ('in_progress', 'В обробці'),
        ('waiting_for_payment', 'Очікується оплата'),
        ('in_delivery', 'Відправлено'),
        ('completed', 'Завершено'),
        ('canceled', 'Скасовано')
    )
    
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
    status = models.CharField(verbose_name='Статус', max_length=100, choices=STATUC_CHOICES, default='in_progress', null=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):  
        return f'Замовлення №{self.id}'
    
    def delete(self):
        for item in self.products.all():
            item.product.quantity += item.quantity
            item.product.save()
        super().delete()

    def get_status(self):
        return dict(self.STATUC_CHOICES)[self.status]  

class OrderIceCream(models.Model):
    order = models.ForeignKey(Order, related_name="ice_cream", on_delete=models.CASCADE)
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.ice_cream.name} - {self.quantity}'