# Generated by Django 3.2.7 on 2021-10-15 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_alter_doctor_doctor_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='fullname',
            new_name='username',
        ),
    ]
