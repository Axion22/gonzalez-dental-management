# Generated by Django 3.2.7 on 2021-12-10 06:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0105_auto_20211210_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpatient',
            name='patient_religion',
            field=models.CharField(max_length=30, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_religion',
            field=models.CharField(max_length=30, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
