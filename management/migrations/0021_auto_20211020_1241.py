# Generated by Django 3.2.7 on 2021-10-20 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0020_alter_inventory_unit_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='exp_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(null=True),
        ),
    ]