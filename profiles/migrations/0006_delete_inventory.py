# Generated by Django 4.0.5 on 2022-06-16 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_inventory_item_alter_inventory_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
