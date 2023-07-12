from django.db import models
from django.contrib.auth.models import User

from ice_cream.models import IceCream
# Create your models here.

class Cart(models.Model):
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.ice_cream.name} - {self.quantity}'