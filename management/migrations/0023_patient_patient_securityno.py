# Generated by Django 3.2.7 on 2021-10-20 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0022_auto_20211020_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_securityNo',
            field=models.IntegerField(blank=True, default=112222346),
            preserve_default=False,
        ),
    ]