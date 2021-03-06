# Generated by Django 4.0.5 on 2022-06-16 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0004_alter_inventory_item_alter_inventory_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='item',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemid', to='store.product'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userid', to=settings.AUTH_USER_MODEL),
        ),
    ]
