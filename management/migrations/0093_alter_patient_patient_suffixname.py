# Generated by Django 3.2.7 on 2021-12-04 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0092_alter_patient_patient_suffixname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_suffixName',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
