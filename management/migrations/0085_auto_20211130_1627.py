# Generated by Django 3.2.7 on 2021-11-30 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0084_alter_treatment_treatment_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='treatment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.treatment'),
        ),
        migrations.AlterField(
            model_name='account',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.department'),
        ),
    ]
