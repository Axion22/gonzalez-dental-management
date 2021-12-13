# Generated by Django 3.2.7 on 2021-12-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0089_auto_20211203_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_drugs',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_tabacco',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=60, null=True),
        ),
    ]
