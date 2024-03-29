# Generated by Django 3.2.7 on 2021-10-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0025_auto_20211021_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patient_name',
            new_name='patient_allergyOthers',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='patient_HomePhone',
            new_name='patient_fatherContact',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='patient_Phone',
            new_name='patient_motherContact',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='civil_status',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patient_securityNo',
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_aidsHIVInfection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_alchohol',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_allergyAntibiotics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_allergyAspirin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_allergyLatex',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_allergyLocalAnesthetics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_allergyMint',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_asthma',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_birthPlace',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_bleedingDisorder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_convulsion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_devAbnormalities',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_diabetes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_drugs',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_fatherName',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_fatherOccupation',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_fathernationality',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_firstName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_glandularProblem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_hearthProblem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_highBloodPressure',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_historyothers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_hospitalization',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_kidneyProblem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_lastDentalVisit',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_lastName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_lastTreatmentDone',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_liverProblem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_lowBloodPressure',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_lungProblem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_medications',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_middleName',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_motherName',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_motherOccupation',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_mothernationality',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_nationality',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_officeAddress',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_personToCall',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_personToCallAddress',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_personToCallPhone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_personToCallRelation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_personToCallWorkTel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_previousDentist',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_previousDoctor',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_religion',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_respiratoryProblems',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_rheurnaticFever',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_seizures',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_specialty',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_strokes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_tabacco',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_thyroidProblem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_tuberculosis',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_whatDrugs',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
