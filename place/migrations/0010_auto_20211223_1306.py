# Generated by Django 3.2.7 on 2021-12-23 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('place', '0009_auto_20211223_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.PositiveIntegerField(blank=True, null=True, verbose_name='Общая сумма')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_finish', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderproduct', to='place.tour')),
            ],
            options={
                'verbose_name': 'Заказ тура',
                'verbose_name_plural': 'Заказ тура',
            },
        ),
        migrations.RemoveField(
            model_name='carttour',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='carttour',
            name='tour',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart_tour',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tours',
        ),
        migrations.RemoveField(
            model_name='ordertour',
            name='order',
        ),
        migrations.RemoveField(
            model_name='ordertour',
            name='tour',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartTour',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderTour',
        ),
    ]
