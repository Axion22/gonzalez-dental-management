# Generated by Django 3.2.7 on 2021-10-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=50, null=True)),
                ('unit_prize', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('exp_date', models.DateTimeField(max_length=50, null=True)),
                ('company_name', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
