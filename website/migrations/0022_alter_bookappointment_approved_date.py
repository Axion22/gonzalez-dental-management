# Generated by Django 3.2.7 on 2021-12-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_alter_bookappointment_your_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointment',
            name='approved_date',
            field=models.DateField(max_length=60, null=True),
        ),
    ]
