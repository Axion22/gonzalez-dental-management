# Generated by Django 3.2.7 on 2021-11-12 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0060_delete_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='doctor_name',
        ),
        migrations.AddField(
            model_name='payment',
            name='full_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.account'),
        ),
    ]