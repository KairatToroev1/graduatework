# Generated by Django 3.2.7 on 2021-12-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_auto_20211220_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='Изображение'),
        ),
    ]
