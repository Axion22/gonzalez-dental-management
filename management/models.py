from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField
from simple_history.models import HistoricalRecords




class Department(models.Model):
  department = models.CharField(max_length=60, null = True)
  description = models.TextField()
  date_created = models.DateTimeField(auto_now_add = True, null = True)

  history = HistoricalRecords(cascade_delete_history=True)
  
  def __str__(self):
    return self.department
    
class Treatment(models.Model): 
  department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
  treatment = models.CharField(max_length=60, null = True)
  treatment_fee = models.IntegerField(null=True, default=0)
  date_created = models.DateTimeField(auto_now_add = True, null = True, blank=True)

  history = HistoricalRecords(cascade_delete_history=True)
  def __str__(self):
    return self.treatment

class Day(models.Model):
  day = models.CharField(max_length=200, null = True)
  
  def __str__(self):
    return self.day
    
class Account(models.Model):
  user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
  full_name = models.CharField(max_length=200, null = True)
  department = models.ForeignKey(Department, blank = True, null=True, on_delete = models.SET_NULL)
  treatment = models.ForeignKey(Treatment, blank = True, null=True, on_delete = models.SET_NULL)
  Time = (
  ('9 AM','9 am'),
  ('10 AM','10 am'),
  ('11 AM','11 am'),
  ('12 PM','12 pm'),
  ('1 PM','1 pm'),
  ('2 PM','2 pm'),
  ('3 PM','3 pm'),
  ('4 PM','4 pm'),
  ('5 PM','5 pm'),

  )
  schedule_time_In = models.CharField(max_length=50, choices=Time, null = True)
  schedule_time_Out = models.CharField(max_length=50, choices=Time, null = True)

  schedule_day = ManyToManyField(Day, blank = True)
  address = models.TextField(max_length=50, null = True)
  phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
  phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, null = True)



  def __str__(self):
      return self.user.first_name+ " " + self.user.last_name


class Patient(models.Model):
  #Patient Information
  patient_lastName = models.CharField(max_length=50, null = True)
  patient_firstName = models.CharField(max_length=50, null = True)
  patient_middleName = models.CharField(max_length=50, null = True)
  patient_suffixName = models.CharField(max_length=25,  blank=True)


  
  patient_age = models.IntegerField(null=True, default=0)
  GENDER = (
  ('male','Male'),
  ('female','Female'),
  )
  patient_sex = models.CharField(max_length=10, null = True, choices=GENDER)
  birth_date = models.DateField( null = True)
  patient_weight = models.FloatField(null=True, blank = True)
  patient_height = models.DecimalField(max_digits = 5, decimal_places = 2,null=True, blank = True)
  patient_religion = models.CharField(max_length=30, null = True)
  patient_nationality = models.CharField(max_length=30, null = True)
  patient_address = models.TextField()
  patient_phone = models.BigIntegerField(null = True)
  
  patient_occupation = models.CharField(max_length=50, null = True)
  patient_company_name = models.CharField(max_length=50, null = True)
  patient_personToCall = models.CharField(max_length=50, null = True, blank = True)
  patient_personToCallRelation = models.CharField(max_length=50, null = True, blank = True)
  patient_personToCallAddress = models.CharField(max_length=100, null = True, blank = True)
  patient_personToCallPhone = models.BigIntegerField(null = True, blank = True)
  patient_personToCallWorkTel = models.BigIntegerField(null = True, blank = True)
  patient_complaint = models.TextField()
  refferedBy = models.CharField(max_length=50, null = True, blank = True)
  
  patient_fatherName = models.CharField(max_length=60, null = True, blank = True)
  patient_fatherOccupation = models.CharField(max_length=60, null = True, blank = True)
  patient_fathernationality = models.CharField(max_length=30, null = True, blank = True)
  patient_fatherContact = models.BigIntegerField( null = True, blank = True)
  patient_fatherOfficeContact = models.BigIntegerField( null = True, blank = True)

  patient_motherName = models.CharField(max_length=60, null = True, blank = True)
  patient_motherOccupation = models.CharField(max_length=60, null = True, blank = True)
  patient_mothernationality = models.CharField(max_length=30, null = True, blank = True)
  patient_motherContact = models.BigIntegerField( null = True, blank = True)
  patient_motherOfficeContact = models.BigIntegerField( null = True, blank = True)

  #Patient Dental History
  patient_previousDentist = models.CharField(max_length=60, null = True, blank = True)
  patient_lastDentalVisit = models.DateField( null = True, blank = True)
  patient_lastTreatmentDone = models.CharField(max_length=60, null = True, blank = True)

  #Patient Medical History
  patient_previousDoctor = models.CharField(max_length=60, null = True, blank = True)
  patient_specialtyDoctor = models.CharField(max_length=60, null = True, blank = True)
  patient_officeAddressDoctor = models.CharField(max_length=100, null = True, blank = True)

  patient_medications = models.CharField(max_length=60, null = True, blank = True)
  patient_hospitalization = models.CharField(max_length=60, null = True, blank = True)
  patient_devAbnormalities = models.CharField(max_length=60, null = True, blank = True)
  patient_allergyLocalAnesthetics = models.BooleanField(default=False)
  patient_allergyAntibiotics = models.BooleanField(default=False)
  patient_allergyAspirin = models.BooleanField(default=False)
  patient_allergyLatex = models.BooleanField(default=False)
  patient_allergyMint = models.BooleanField(default=False)
  patient_allergyOthers = models.CharField(max_length=60, null = True, blank = True)
  yesno = (
    ('yes','Yes'),
    ('no','No'),
    )
  patient_tabacco = models.CharField(max_length=60, null = True, blank = True,choices=yesno)
  patient_drugs = models.CharField(max_length=60, null = True, blank = True,choices=yesno)
  

  patient_highBloodPressure = models.BooleanField(default=False)
  patient_lowBloodPressure = models.BooleanField(default=False)
  patient_respiratoryProblems = models.BooleanField(default=False)
  patient_bleedingDisorder = models.BooleanField(default=False)
  patient_convulsion = models.BooleanField(default=False)
  patient_asthma = models.BooleanField(default=False)
  patient_rheurnaticFever = models.BooleanField(default=False)
  patient_glandularProblem = models.BooleanField(default=False)
  patient_aidsHIVInfection = models.BooleanField(default=False)
  patient_strokes = models.BooleanField(default=False)
  patient_diabetes = models.BooleanField(default=False)
  patient_seizures = models.BooleanField(default=False)
  patient_lungProblem = models.BooleanField(default=False)
  patient_liverProblem = models.BooleanField(default=False)
  patient_kidneyProblem = models.BooleanField(default=False)
  patient_hearthProblem = models.BooleanField(default=False)
  patient_thyroidProblem = models.BooleanField(default=False)
  patient_tuberculosis = models.BooleanField(default=False)
  patient_historyothers = models.CharField(max_length=60, null = True, blank = True)
  

  history = HistoricalRecords(cascade_delete_history=True)
  date_created = models.DateTimeField(auto_now_add = True, null = True)

  def __str__(self):
    return self.patient_firstName + " " + self.patient_middleName +" " + self.patient_lastName + " " + self.patient_suffixName



class Payment(models.Model):
  patient_name = models.ForeignKey(Patient, null=True, on_delete = models.SET_NULL)
  doctor_name = models.ForeignKey(Account, null=True, on_delete = models.SET_NULL)
  department = models.ForeignKey(Department, null=True, on_delete = models.SET_NULL)
  treatment = models.ForeignKey(Treatment, null=True, on_delete = models.SET_NULL)
  tooth_number = models.CharField(max_length=20, null=True )
  payment_date = models.DateField( null = True)
  METHOD = (
    ('cash','Cash'),
    ('installment','Installment'),
    ('check','Check'),
    ('online','Online'),
    )
  method = models.CharField(max_length=20, null = True, choices=METHOD)

  STATUS = (
    ('paid','Paid'),
    ('unpaid','Unpaid'),
    )
  status = models.CharField(max_length=20, null = True, choices=STATUS)

  fee =  models.IntegerField(null=True, default=0)
  balance =  models.IntegerField(null=True, default=0)
  date_created = models.DateTimeField(auto_now_add = True, null = True)
  history = HistoricalRecords(cascade_delete_history=True)


  def __str__(self):
      return self.patient_name.patient_lastName




class Inventory(models.Model):
  product_name = models.CharField(max_length=50, null = True)
  company_name = models.CharField(max_length=50, null = True)
  phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
  company_contact = models.CharField(validators = [phoneNumberRegex], max_length = 12, default=0)
  unit_prize = models.IntegerField( null = True, default=0 )
  exp_date = models.DateField( null = True )
  quantity = models.IntegerField( null=True, default=0 )
  reorder_level = models.IntegerField(default='0', blank=True, null=True)

  receive_quantity = models.IntegerField(default='0', blank=True, null=True)
  receive_by = models.ForeignKey(Account, related_name='staff', null=True, on_delete = models.SET_NULL)

  issue_quantity = models.IntegerField(default='0', blank=True, null=True)
  issue_to = models.ForeignKey(Account, related_name='doctor',max_length=50, blank=True, null=True, on_delete = models.SET_NULL)
  issue_by = models.CharField(max_length=50, null = True)
  last_updated = models.DateTimeField(auto_now_add = True, null = True)

  date_created = models.DateTimeField(auto_now_add = True, null = True)
  history = HistoricalRecords(cascade_delete_history=True)
  
  class Meta:
    ordering = ('product_name',)

  def __str__(self):
      return self.product_name























