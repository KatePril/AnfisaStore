from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('name', 'image_tag_thumbnail')
    prepopulated_fields = {'slug': ('name',)}

    readonly_fields = ('image_tag_thumbnail',)
    fields = ('name', 'slug', 'parent', 'description','image_tag_thumbnail', 'image',
                'meta_title', 'meta_description', 'meta_keywords')