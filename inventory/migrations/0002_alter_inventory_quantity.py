# Generated by Django 4.0.5 on 2022-06-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=5.0, max_digits=5),
        ),
    ]