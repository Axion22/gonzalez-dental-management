# Generated by Django 3.2.7 on 2021-10-25 09:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0035_alter_inventory_company_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='company_contact',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
