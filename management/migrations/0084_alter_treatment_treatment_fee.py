# Generated by Django 3.2.7 on 2021-11-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0083_auto_20211122_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='treatment_fee',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
