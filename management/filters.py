from django.db.models.fields import Field
from django.db.models.query_utils import Q
import django_filters
from .models import *
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput, TextInput
from website.models import BookAppointment, VirtualConsult

class InventoryFilter(django_filters.FilterSet):
  inventorySearch = CharFilter(method='my_custom_filter',label="Search", lookup_expr = 'icontains',widget=TextInput(attrs={'placeholder': 'Search...','class':'form-control input-sm' }))



  class Meta:
    model = Inventory
    fields = ['id','product_name','company_name']

  def my_custom_filter(self, queryset, name, value):
        return Inventory.objects.filter(
            Q(id__icontains=value) | 
            Q(product_name__icontains=value) | 
            Q(company_name__icontains=value) 
        )

class PatientFilter(django_filters.FilterSet):
  id = CharFilter(label="Search", lookup_expr = 'icontains' , widget=TextInput(attrs={'placeholder': 'id...','class':'form-control input-sm', 'type':'text' }))
  patient_name = CharFilter(method="my_custom_filter1",label="Search", lookup_expr = 'icontains' , widget=TextInput(attrs={'placeholder': 'Patient...','class':'form-control input-sm', 'type':'text' }))

  
  class Meta:
    model = Patient
    fields = ['id','patient_name',]

  def my_custom_filter1(self, queryset, name, value):
        return Patient.objects.filter(
            Q(patient_lastName__icontains=value) | 
            Q(patient_firstName__icontains=value) | 
            Q(patient_middleName__icontains=value)
        )
        
class BookAppointmentFilter(django_filters.FilterSet):
  id = CharFilter(label="Search", lookup_expr = 'icontains' , widget=TextInput(attrs={'placeholder': 'id...','class':'form-control input-sm', 'type':'text' }))
  
  name = CharFilter(method="my_custom_filter3",label="Search", lookup_expr = 'icontains' , widget=TextInput(attrs={'placeholder': 'Patient...','class':'form-control input', 'type':'text' }))
  
  approved_date = DateFilter(label="Search", lookup_expr = 'icontains' , widget=DateInput(format=('%Y-%m-%d'),
        attrs={'class': 'form-control input-height-sm', 
               'placeholder': 'Select a date',
               'type': 'date'
              }))


  class Meta:
    model = BookAppointment
    fields = [ 'id','first_name', 'last_name', 'approved_date']

  def my_custom_filter3(self, queryset, name, value):
        return BookAppointment.objects.filter(
            Q(last_name__icontains=value) | 
            Q(first_name__icontains=value) 
        )
        
        

class PaymentFilter(django_filters.FilterSet):

  patient_name = CharFilter(method="my_custom_filter",label="Search", lookup_expr = 'icontains' , widget=TextInput(attrs={'placeholder': 'Patient...','class':'form-control input-sm', 'type':'text' }))
  doctor_name__full_name = CharFilter(label="Search", lookup_expr = 'icontains' , widget=TextInput(attrs={'placeholder': 'Doctor...','class':'form-control input-sm', 'type':'text' }))
  
  class Meta:
    model = Payment
    fields = ['patient_name','doctor_name__full_name']
    
  def my_custom_filter(self, queryset, name, value):
        return Payment.objects.filter(
            Q(patient_name__patient_lastName__icontains=value) | Q(patient_name__patient_firstName__icontains=value)
        )
    




