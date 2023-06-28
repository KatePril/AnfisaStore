from django.contrib import admin

from .models import IceCream, Image

class ImageInline(admin.TabularInline):
    model = Image
    fields = ('ice_cream','image_tag')
    readonly_fileds = ('image_tag',)
    extra = 1

admin.site.register(Image)
@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'quantity', 'price')
    inlines = (ImageInline,)