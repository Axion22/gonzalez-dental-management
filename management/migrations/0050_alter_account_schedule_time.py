# Generated by Django 3.2.7 on 2021-11-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0049_auto_20211103_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='schedule_time',
            field=models.TimeField(max_length=50, null=True),
        ),
    ]
