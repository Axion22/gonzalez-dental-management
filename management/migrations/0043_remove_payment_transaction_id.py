# Generated by Django 3.2.7 on 2021-10-28 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0042_alter_patient_patient_height'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='transaction_id',
        ),
    ]
