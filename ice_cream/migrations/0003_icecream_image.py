# Generated by Django 4.2.2 on 2023-06-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_alter_icecream_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ice_cream/', verbose_name='Зображення'),
        ),
    ]
