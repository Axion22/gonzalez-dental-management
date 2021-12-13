# Generated by Django 3.2.7 on 2021-10-15 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_rename_treatments_department_treatment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_name',
        ),
        migrations.AddField(
            model_name='account',
            name='fullname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='fullname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.account'),
        ),
    ]