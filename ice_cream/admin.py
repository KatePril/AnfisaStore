from django.contrib import admin

from .models import IceCream, Image

class IceCreamCategoryInline(admin.TabularInline):
    model = IceCream.category.through
    extra = 1

class ImageInline(admin.TabularInline):
    model = Image
    fields = ('ice_cream', 'image', 'is_main')
    # readonly_fileds = ('image_tag_thumbnail',)
    extra = 1

admin.site.register(Image)
@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'quantity', 'price', 'on_main',
            'meta_title', 'meta_description', 'meta_keywords')
    inlines = (ImageInline, IceCreamCategoryInline)