# Generated by Django 3.2.7 on 2021-12-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0013_alter_tour_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='number_telefon',
            field=models.IntegerField(default=0),
        ),
    ]
