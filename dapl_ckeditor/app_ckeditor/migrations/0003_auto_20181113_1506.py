# Generated by Django 2.0 on 2018-11-13 15:06

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ckeditor', '0002_auto_20181113_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(blank=True, default='', storage=django.core.files.storage.FileSystemStorage(location='/home/dat-asset-09/code/Django-Ckeditor/dapl_ckeditor/media'), upload_to=''),
        ),
    ]
