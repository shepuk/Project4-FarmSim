# Generated by Django 4.0.5 on 2022-06-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0003_alter_farm_crop2_alter_farm_crop3_alter_farm_crop4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='crop1_plant_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='crop2_plant_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='crop3_plant_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='crop4_plant_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='crop5_plant_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='crop6_plant_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='crop7_plant_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='crop8_plant_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
