# Generated by Django 3.2.7 on 2021-10-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0038_auto_20211026_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patient_whatDrugs',
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_alchohol',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_drugs',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_tabacco',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
