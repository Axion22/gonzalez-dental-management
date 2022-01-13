from django.db import models
from django.core.validators import RegexValidator
from management.models import Account

class BookAppointment(models.Model): 
  first_name = models.CharField(max_length=60, null = True)
  last_name = models.CharField(max_length=60, null = True)
  phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
  your_phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, null = True)
  your_email = models.CharField(max_length=60, null = True)
  service_required = models.CharField(max_length=60, null = True)
  your_schedule = models.CharField(max_length=60, null = True)
  your_date = models.DateField( null = True)
  your_message = models.TextField( blank=True)
  approved_date = models.DateField(max_length=60, null = True)
  approved_time = models.CharField(max_length=60, null = True)
  assign_doctor = models.ForeignKey(Account, null=True, on_delete = models.SET_NULL)
  accepted = models.BooleanField(default=False)
  accepted_date = models.DateTimeField(auto_now_add = False , null = True)
  done = models.BooleanField(default=False)
  
  date_created = models.DateTimeField(auto_now_add = True)
  
  class Meta:
    ordering = ('-date_created',)
    
  def __str__(self):
    return self.first_name
  
        
  
class VirtualConsult(models.Model): 
  first_name = models.CharField(max_length=60, null = True)
  last_name = models.CharField(max_length=60, null = True)
  
  full_face = models.ImageField(null = True, blank=True, upload_to="images/")
  close_up = models.ImageField(null = True, blank=True, upload_to="images/")
  
  phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
  phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, null = True)
  email = models.CharField(max_length=60, null = True)
  message = models.TextField( blank=True)
  my_message = models.TextField( blank=True)
  date_created = models.DateTimeField(auto_now_add = True)
  assign_doctor = models.ForeignKey(Account, null=True, on_delete = models.SET_NULL)
  assigned = models.BooleanField(default=False)
  
  accepted = models.BooleanField(default=False)
  accepted_date = models.DateTimeField(auto_now_add = False , null = True)
  is_deleted = models.BooleanField(default=False)
  
  class Meta:
    ordering = ('-date_created',)
    
  def __str__(self):
    return self.first_name


class Contact(models.Model): 
  name = models.CharField(max_length=200, null = True)
  email = models.CharField(max_length=100, null = True)
  message = models.TextField( blank=True)
  my_message = models.TextField( blank=True)
  date_created = models.DateTimeField(auto_now_add = True)

  
  def __str__(self):
    return self.name  
  


