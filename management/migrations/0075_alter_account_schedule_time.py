# Generated by Django 3.2.7 on 2021-11-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0074_auto_20211116_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='schedule_time',
            field=models.CharField(choices=[('10 AM', '10 am'), ('11 AM', '11 am'), ('12 PM', '12 pm'), ('1 PM', '1 pm'), ('2 PM', '2 pm'), ('3 PM', '3 pm'), ('4 PM', '4 pm')], max_length=50, null=True),
        ),
    ]