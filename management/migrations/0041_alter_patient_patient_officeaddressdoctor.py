# Generated by Django 3.2.7 on 2021-10-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0040_remove_patient_patient_alchohol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_officeAddressDoctor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]