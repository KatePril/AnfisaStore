from django.contrib import admin

# Register your models here
from .models import Order, OrderIceCream

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total', 'first_name', 'last_name', 'email', 'address', 'comments', 'created', 'updated', 'paid']
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['paid']    
    search_fields = ['id', 'total', 'first_name', 'last_name', 'email', 'address', 'comments', 'created', 'updated', 'paid']

@admin.register(OrderIceCream)
class OrderIceCreamAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'ice_cream', 'price', 'quantity']
    list_filter = ['order', 'ice_cream', 'price', 'quantity']
    list_editable = ['price', 'quantity']    
    search_fields = ['id', 'order', 'ice_cream', 'price', 'quantity']