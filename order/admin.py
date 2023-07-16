from django.contrib import admin

# Register your models here
from .models import Order, OrderIceCream

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created', 'updated']
    list_filter = ['user', 'status', 'created', 'updated']
    list_editable = ['status']    
    search_fields = ['id', 'user', 'status', 'created', 'updated']

@admin.register(OrderIceCream)
class OrderIceCreamAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'ice_cream', 'price', 'quantity']
    list_filter = ['order', 'ice_cream', 'price', 'quantity']
    list_editable = ['price', 'quantity']    
    search_fields = ['id', 'order', 'ice_cream', 'price', 'quantity']