# Generated by Django 3.2.7 on 2021-12-03 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0086_payment_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ('-exp_date',)},
        ),
    ]
