from django.contrib import admin

from .models import IceCream

# admin.site.register(IceCream)
@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    pass