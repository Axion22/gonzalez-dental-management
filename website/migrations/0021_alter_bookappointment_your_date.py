# Generated by Django 3.2.7 on 2021-12-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20211211_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointment',
            name='your_date',
            field=models.DateField(null=True),
        ),
    ]
