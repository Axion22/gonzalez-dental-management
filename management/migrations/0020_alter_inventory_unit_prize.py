# Generated by Django 3.2.7 on 2021-10-19 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_inventory_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='unit_prize',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
