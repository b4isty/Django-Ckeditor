# Generated by Django 2.0 on 2018-11-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ckeditor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
