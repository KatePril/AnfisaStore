# Generated by Django 4.2.2 on 2023-07-02 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
