# Generated by Django 3.2.7 on 2021-11-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0047_doctor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_schedule',
            field=models.TimeField(max_length=50, null=True),
        ),
    ]
