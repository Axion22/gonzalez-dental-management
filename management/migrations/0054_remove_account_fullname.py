# Generated by Django 3.2.7 on 2021-11-03 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0053_auto_20211103_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='fullname',
        ),
    ]