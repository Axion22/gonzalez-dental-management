# Generated by Django 3.2.7 on 2021-11-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0081_alter_inventory_unit_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='fee',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
