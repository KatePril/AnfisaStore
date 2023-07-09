from django.contrib.admin import display
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe
from django.urls import reverse
from catalog.models import Category

class IceCream(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    on_main = models.BooleanField('На главную?', default=True)
    # image = models.ImageField(upload_to='ice_cream/', verbose_name='Зображення', blank=True, null=True)

    category = models.ManyToManyField(
            to=Category,
            verbose_name='Категории',
            through='IceCreamCategory',
            related_name='ice_cream',
            blank=True        
        )

    class Meta:        
        ordering = ('name',)
        verbose_name = 'мороженое'
        verbose_name_plural = 'мороженое'

    def __str__(self):
        return f'{self.name}'
    
    def images(self):
        return Image.objects.filter(ice_cream=self.id)

    def main_image(self):
        image = Image.objects.filter(ice_cream=self.id, is_main=True)
        if image:
            return image.first()
        return self.images().first()

    def get_absolute_url(self):
        return reverse('ice_cream', kwargs={'pk': self.id})

class Image(models.Model):
    image = ProcessedImageField(
        upload_to = 'media/ice_cream',
        processors=[],
        format='JPEG',
        options={'quality': 70},
        null=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 200)],
        format='JPEG',
        options={'quality': 70}
    )
    ice_cream = models.ForeignKey(
        to=IceCream,
        on_delete=models.CASCADE,
        related_name='images'
    )
    is_main = models.BooleanField(verbose_name='Основне', default=False)
    
    @display(description='Зображення')
    def image_tag_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                Image.objects.get(id=self.id)
            return mark_safe(f'<img src="{self.image_thumbnail.url}" height="70">')
        
    @display(description='Зображення')
    def image_tag(self):
        if self.image:
            if not self.image_thumbnail:
                Image.objects.get(id=self.id)
            return mark_safe(f'<img src="{self.image_thumbnail.url}">')

class IceCreamCategory(models.Model):
    product = models.ForeignKey(IceCream, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_main = models.BooleanField( default=False)

    def __str__(self):
        return f'{self.product.name} - {self.category.name}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_main:
            IceCreamCategory.objects.filter(product=self.product, is_main=True).update(is_main=False)
        super().save(force_insert, force_update, using, update_fields)