# Generated by Django 3.2.7 on 2021-11-12 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0065_alter_inventory_issue_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='receive_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.staff'),
        ),
    ]