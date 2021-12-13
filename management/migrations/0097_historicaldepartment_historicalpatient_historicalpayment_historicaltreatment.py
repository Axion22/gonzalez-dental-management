# Generated by Django 3.2.7 on 2021-12-07 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0096_historicalinventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTreatment',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('treatment', models.CharField(max_length=60, null=True)),
                ('treatment_fee', models.IntegerField(default=0, null=True)),
                ('date_created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('department', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='management.department')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical treatment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPayment',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('payment_date', models.DateField(null=True)),
                ('method', models.CharField(choices=[('cash', 'Cash'), ('installment', 'Installment'), ('check', 'Check'), ('online', 'Online')], max_length=20, null=True)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], max_length=20, null=True)),
                ('fee', models.IntegerField(default=0, null=True)),
                ('balance', models.IntegerField(default=0, null=True)),
                ('date_created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('department', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='management.department')),
                ('doctor_name', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='management.account')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('patient_name', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='management.patient')),
                ('treatment', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='management.treatment')),
            ],
            options={
                'verbose_name': 'historical payment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPatient',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('patient_lastName', models.CharField(max_length=50, null=True)),
                ('patient_firstName', models.CharField(max_length=50, null=True)),
                ('patient_middleName', models.CharField(max_length=50, null=True)),
                ('patient_suffixName', models.CharField(blank=True, max_length=25)),
                ('patient_age', models.IntegerField(default=0, null=True)),
                ('patient_sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('patient_weight', models.FloatField(blank=True, null=True)),
                ('patient_height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('patient_religion', models.CharField(max_length=30, null=True)),
                ('patient_nationality', models.CharField(max_length=30, null=True)),
                ('patient_address', models.TextField()),
                ('patient_phone', models.BigIntegerField(null=True)),
                ('patient_occupation', models.CharField(max_length=50, null=True)),
                ('patient_company_name', models.CharField(max_length=50, null=True)),
                ('patient_personToCall', models.CharField(blank=True, max_length=50, null=True)),
                ('patient_personToCallRelation', models.CharField(blank=True, max_length=50, null=True)),
                ('patient_personToCallAddress', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_personToCallPhone', models.BigIntegerField(blank=True, null=True)),
                ('patient_personToCallWorkTel', models.BigIntegerField(blank=True, null=True)),
                ('patient_complaint', models.TextField()),
                ('refferedBy', models.CharField(blank=True, max_length=50, null=True)),
                ('patient_fatherName', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_fatherOccupation', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_fathernationality', models.CharField(blank=True, max_length=30, null=True)),
                ('patient_fatherContact', models.BigIntegerField(blank=True, null=True)),
                ('patient_fatherOfficeContact', models.BigIntegerField(blank=True, null=True)),
                ('patient_motherName', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_motherOccupation', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_mothernationality', models.CharField(blank=True, max_length=30, null=True)),
                ('patient_motherContact', models.BigIntegerField(blank=True, null=True)),
                ('patient_motherOfficeContact', models.BigIntegerField(blank=True, null=True)),
                ('patient_previousDentist', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_lastDentalVisit', models.DateField(blank=True, null=True)),
                ('patient_lastTreatmentDone', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_previousDoctor', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_specialtyDoctor', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_officeAddressDoctor', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_medications', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_hospitalization', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_devAbnormalities', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_allergyLocalAnesthetics', models.BooleanField(default=False)),
                ('patient_allergyAntibiotics', models.BooleanField(default=False)),
                ('patient_allergyAspirin', models.BooleanField(default=False)),
                ('patient_allergyLatex', models.BooleanField(default=False)),
                ('patient_allergyMint', models.BooleanField(default=False)),
                ('patient_allergyOthers', models.CharField(blank=True, max_length=60, null=True)),
                ('patient_tabacco', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=60, null=True)),
                ('patient_drugs', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=60, null=True)),
                ('patient_highBloodPressure', models.BooleanField(default=False)),
                ('patient_lowBloodPressure', models.BooleanField(default=False)),
                ('patient_respiratoryProblems', models.BooleanField(default=False)),
                ('patient_bleedingDisorder', models.BooleanField(default=False)),
                ('patient_convulsion', models.BooleanField(default=False)),
                ('patient_asthma', models.BooleanField(default=False)),
                ('patient_rheurnaticFever', models.BooleanField(default=False)),
                ('patient_glandularProblem', models.BooleanField(default=False)),
                ('patient_aidsHIVInfection', models.BooleanField(default=False)),
                ('patient_strokes', models.BooleanField(default=False)),
                ('patient_diabetes', models.BooleanField(default=False)),
                ('patient_seizures', models.BooleanField(default=False)),
                ('patient_lungProblem', models.BooleanField(default=False)),
                ('patient_liverProblem', models.BooleanField(default=False)),
                ('patient_kidneyProblem', models.BooleanField(default=False)),
                ('patient_hearthProblem', models.BooleanField(default=False)),
                ('patient_thyroidProblem', models.BooleanField(default=False)),
                ('patient_tuberculosis', models.BooleanField(default=False)),
                ('patient_historyothers', models.CharField(blank=True, max_length=60, null=True)),
                ('date_created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical patient',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDepartment',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('department', models.CharField(max_length=60, null=True)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical department',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
