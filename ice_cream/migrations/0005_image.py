# Generated by Django 4.2.2 on 2023-06-27 18:46

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0004_icecream_price_icecream_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(null=True, upload_to='media/ice_cream')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основне')),
                ('ice_cream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ice_cream.icecream')),
            ],
        ),
    ]
