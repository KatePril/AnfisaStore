# Generated by Django 4.2.2 on 2023-06-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0003_icecream_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icecream',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
