# Generated by Django 3.2.7 on 2021-11-01 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0043_remove_payment_transaction_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='issue_by',
            new_name='issue_to',
        ),
    ]
