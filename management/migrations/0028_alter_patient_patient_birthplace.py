# Generated by Django 3.2.7 on 2021-10-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0027_alter_patient_patient_historyothers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_birthPlace',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
