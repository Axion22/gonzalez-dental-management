# Generated by Django 3.2.7 on 2021-10-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_auto_20211015_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthistory',
            name='history_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
