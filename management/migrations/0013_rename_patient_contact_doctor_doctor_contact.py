# Generated by Django 3.2.7 on 2021-10-15 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_rename_fullname_doctor_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='patient_contact',
            new_name='doctor_contact',
        ),
    ]
