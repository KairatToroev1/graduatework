# Generated by Django 3.2.7 on 2021-12-20 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20211220_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='movie',
            new_name='tour',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='ip',
        ),
    ]
