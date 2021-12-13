# Generated by Django 3.2.7 on 2021-12-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0087_alter_inventory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_suffixName',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_firstName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_lastName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_middleName',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
