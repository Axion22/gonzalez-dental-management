# Generated by Django 3.2.7 on 2021-11-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0054_remove_account_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='schedule_day',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=50, null=True),
        ),
    ]