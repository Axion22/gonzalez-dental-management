from django.contrib.messages.api import error
from django.db.models import fields
from django.contrib.admin.widgets import AutocompleteSelect
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django import forms
from .models import *
from website.models import *


class CreateUserForm(UserCreationForm):
  password1 = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control','type':'password' }))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control','type':'password' }))
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    widgets = {
      'username' : forms.TextInput(attrs = {'class':'form-control' }),
      'email' : forms.TextInput(attrs = {'class':'form-control' }),
      'first_name' : forms.TextInput(attrs = {'class':'form-control' }),
      'last_name' : forms.TextInput(attrs = {'class':'form-control' }),
      'password1' : forms.TextInput(attrs = {'class':'form-control' ,'type':'password' }),
      'password2' : forms.TextInput(attrs = {'class':'form-control' ,'type':'password' }),

    }

class accountForm(forms.ModelForm):
  class Meta:
    
    model = Account
    fields = [ 'full_name', 'department','treatment', 'schedule_time_In','schedule_time_Out', 'schedule_day', 'address', 'phone' ]

    exclude = ['user']
    widgets = {
    'full_name': forms.TextInput(attrs = {'class':'form-control' }),
    'department': forms.Select(attrs = {'class':'form-control' }),
    'treatment': forms.Select(attrs = {'class':'form-control' }),
    'schedule_time_In': forms.Select(attrs = {'class':'form-control'}),
    'schedule_time_Out': forms.Select(attrs = {'class':'form-control'}),
    'schedule_day': forms.CheckboxSelectMultiple(attrs = {'style':'list-style-type: none;'}),
    'address': forms.Textarea(attrs = {'class':'form-control' }),
    'phone': forms.TextInput(attrs = {'class':'form-control' }),
    }
    

class DayForm(forms.ModelForm):
  class Meta:
    model = Day
    fields = '__all__'
    
       
class DepartmentForm(forms.ModelForm):
  class Meta:
    model = Department
    fields = '__all__'
    widgets = {
      'department' : forms.TextInput(attrs = {'class':'form-control' }),
      'description' : forms.Textarea(attrs = {'class':'form-control' }),
      'treatment' : forms.TextInput(attrs = {'class':'form-control' }),
    }
    
class TreatmentForm(forms.ModelForm):
  class Meta:
    model = Treatment
    fields = ['treatment','treatment_fee']
    widgets = {
      'treatment' : forms.TextInput(attrs = {'class':'form-control'}),
      'treatment_fee' : forms.TextInput(attrs = {'class':'form-control' }),
    }
    

TreatmentFormSet = inlineformset_factory(
  Department, Treatment, form = TreatmentForm,
  min_num=20, extra=1, can_delete=False
  
)

class BookAppointmentForm(forms.ModelForm):
  assign_doctor = forms.ModelChoiceField(queryset=Account.objects.all(), empty_label='assign to doctor',widget=forms.Select(attrs = {'class':'form-control','type':'password' }))
  
  #to remove staff
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assign_doctor'].queryset = Account.objects.exclude(
    department=5)
  
  class Meta:
    model = BookAppointment
    fields = ['assign_doctor']
    exclude = ['first_name', 'last_name', 'your_phone', 'your_email', 'service_required', 'your_message', 'approved_date', 'approved_time','your_schedule','your_date','date_created','accepted', 'accepted_date','done']

 
class CreateBookAppointmentForm(forms.ModelForm):
  assign_doctor = forms.ModelChoiceField(queryset=Account.objects.all(), empty_label='assign to doctor',widget=forms.Select(attrs = {'class':'form-control','type':'password' }))
  
  #to remove staff
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assign_doctor'].queryset = Account.objects.exclude(
    department=5)
  
  class Meta:
    model = BookAppointment
    fields = ['first_name', 'last_name', 'your_phone', 'your_email', 'service_required', 'your_message', 'approved_date', 'approved_time','assign_doctor']
    exclude = ['your_schedule','your_date','date_created','accepted', 'accepted_date','done']
    time = (('', 'time...'),('9:00 am','9:00 am'),('9:30 am','9:30 am'),('10:00 am','10:00 am'),
          ('10:30 am','10:30 am'),('11:00 am','11:00 am'),('11:30 am','11:30 am'),('12:00 pm','12:00 pm'),('12:30 pm','12:30 pm'),('1:00 pm','1:00 pm'),
          ('1:30 pm','1:30 pm'),('2:00 pm','2:00 pm'),('2:30 pm','2:30 pm'),
          ('3:00 pm','3:00 pm'),('3:30 pm','3:30 pm'),('4:00 pm','4:00 pm'),
          ('4:30 pm','4:30 pm'),)
    
    widgets = {
      'first_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'first name...' }),
      'last_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'last name...' }),
      'your_phone': forms.TextInput(attrs = {'class':'form-control','placeholder':'phone...' }),
      'your_email': forms.TextInput(attrs = {'class':'form-control','placeholder':'email...' }),
      'service_required': forms.TextInput(attrs = {'class':'form-control','placeholder':'service required...' }),
      'approved_time': forms.Select(choices=time,attrs = {'class':'form-control','placeholder':'time...' }),
      
      'your_message': forms.Textarea( attrs = {'class':'form-control','placeholder':'Comment...' }),
      'approved_date': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
    }    


class VirtualConsultationForm(forms.ModelForm):
  
  #to remove staff
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assign_doctor'].queryset = Account.objects.exclude(
    department=5)
  class Meta:
    model = VirtualConsult
    fields = '__all__'
    exclude = ['first_name', 'last_name', 'full_face', 'close_up', 'phone', 'email', 'message', 'my_message', 'date_created', 'accepted', 'accepted_date',]
    
    widgets = {
      'assign_doctor' : forms.Select(attrs = {'class':'form-control' }),
    }   
    
    
class ContactForm(forms.ModelForm):
  class Meta:
     model = Contact
     fields = '__all__'
     exclude = ['name', 'email', 'message']
     
     widgets = {
      'assign_doctor' : forms.Select(attrs = {'class':'form-control' }),
    }  

class PatientForm(forms.ModelForm):
  
  def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(PatientForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['patient_suffixName'].required = False
        
  class Meta:
    model = Patient
    fields = '__all__'
    widgets = {
      'patient_lastName': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_firstName' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_middleName' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_suffixName' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_age' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_sex' : forms.Select(attrs = {'class':'form-control' }),
      'birth_date' : forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
      'patient_weight' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_height' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_religion' : forms.TextInput(attrs = {'class':'form-control', 'pattern':'[A-Za-z ]+' }),
      'patient_nationality' : forms.TextInput(attrs = {'class':'form-control','pattern':'[A-Za-z ]+' }),
      'patient_address' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_occupation' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_company_name' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_phone' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_personToCall' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_personToCallRelation' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_personToCallAddress' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_personToCallPhone' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_personToCallWorkTel' : forms.TextInput(attrs = {'class':'form-control' }),
      'patient_complaint' : forms.TextInput(attrs = {'class':'form-control' }),
      'refferedBy' : forms.TextInput(attrs = {'class':'form-control' }),

      'patient_fatherName': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_fatherOccupation': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_fathernationality': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_fatherContact': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_fatherOfficeContact': forms.TextInput(attrs = {'class':'form-control' }),
      
      'patient_motherName': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_motherOccupation': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_mothernationality': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_motherContact': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_motherOfficeContact': forms.TextInput(attrs = {'class':'form-control' }),

      'patient_previousDentist': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_lastDentalVisit': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
      'patient_lastTreatmentDone': forms.TextInput(attrs = {'class':'form-control','pattern':'[A-Za-z ]+' }),

      'patient_previousDoctor': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_specialtyDoctor': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_officeAddressDoctor': forms.TextInput(attrs = {'class':'form-control' }),

      'patient_medications': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_hospitalization': forms.TextInput(attrs = {'class':'form-control' }),
      'patient_devAbnormalities': forms.TextInput(attrs = {'class':'form-control' }),

      'patient_allergyLocalAnesthetics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_allergyAntibiotics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_allergyAspirin': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_allergyLatex': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_allergyMint': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

      'patient_allergyOthers': forms.TextInput(attrs = {'class':'form-control' }),

      'patient_tabacco': forms.Select(attrs = {'class':'form-control' }),
      'patient_drugs': forms.Select(attrs = {'class':'form-control' }),

      'patient_highBloodPressure': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_lowBloodPressure': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_respiratoryProblems': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_bleedingDisorder': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_convulsion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_asthma': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_rheurnaticFever': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_glandularProblem': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_aidsHIVInfection': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_strokes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_diabetes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_seizures': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_lungProblem': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_liverProblem': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_kidneyProblem': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_hearthProblem': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_thyroidProblem': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'patient_tuberculosis': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

      'patient_historyothers': forms.TextInput(attrs={'class': 'form-control'}),

    }

class PaymentForm(forms.ModelForm):
  
  #to remove staff
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor_name'].queryset = Account.objects.exclude(
    department=5)
        
  class Meta:
    
    model = Payment
    fields = ['patient_name','doctor_name','department','treatment', 'tooth_number','payment_date','method', 'status', 'fee', 'balance']

    widgets = {
      'patient_name': forms.Select(attrs = {'class':'form-control select2 '}),
      'doctor_name': forms.Select(attrs = {'class':'form-control select2 ' }),
      'department': forms.Select(attrs = {'class':'form-control input-height-sm ' }),
      'treatment' : forms.Select(attrs = {'class':'form-control input-height-sm ' }),
      'tooth_number' : forms.TextInput(attrs = {'class':'form-control input-height-sm' }),
      'payment_date' : forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control input-height-sm', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
      'method' : forms.Select(attrs = {'class':'form-control input-height-sm' }),
      'status': forms.Select(attrs = {'class':'form-control input-height-sm' }),
      'fee' : forms.TextInput(attrs = {'class':'form-control input-height-sm' }),
      'balance' : forms.TextInput(attrs = {'class':'form-control input-height-sm' }),
    }
       
         
    def __init__(self, user=None, **kwargs):
        super(PaymentForm, self).__init__(**kwargs)
        if user:
            self.fields['doctor_name'].queryset = Payment.objects.exclude(doctor_name=['doctor'])
            
    
            

                   
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['treatment'].queryset = Treatment.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['treatment'].queryset = Treatment.objects.filter(department_id=department_id).order_by('department')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['treatment'].queryset = self.instance.department.treatment_set.order_by('treatment')
            
            
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fee'] = Payment.objects.none()

        if 'treatment' in self.data:
            try:
                treatment_id = int(self.data.get('treatment'))
                self.fields['fee'] = Treatment.objects.get(id=treatment_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['fee'] = self.instance.treatment.treatment
            
    
            

    
    

            

class InventoryForm(forms.ModelForm):
  class Meta:
    model = Inventory
    fields = ['product_name','company_name','company_contact','unit_prize','exp_date','quantity']
    widgets = {
      'product_name' : forms.TextInput(attrs = {'class':'form-control input-height' }), 
      'company_name' : forms.TextInput(attrs = {'class':'form-control input-height'}),
      'company_contact' : forms.TextInput(attrs = {'class':'form-control input-height'}), 
      'unit_prize' : forms.TextInput(attrs = {'class':'form-control input-height'}),
      'exp_date' : forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control input-height', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
      'quantity' : forms.TextInput(attrs = {'class':'form-control input-height'}),
      
    }



class InventoryIssueForm(forms.ModelForm):
  class Meta:
    model = Inventory
    fields = ['issue_quantity', 'issue_to']
    widgets = {
      'issue_quantity' : forms.TextInput(attrs = {'class':'form-control input-height'}),
      'issue_to' : forms.Select(attrs = {'class':'form-control input-height'}),
      
    }



class InventoryReceiveForm(forms.ModelForm):
  class Meta:
    model = Inventory
    fields = ['receive_quantity', 'receive_by']
    widgets = {
      'receive_quantity' : forms.TextInput(attrs = {'class':'form-control input-height'}),
      'receive_by' : forms.Select(attrs = {'class':'form-control input-height'}),
      
    }
    
    
class ReorderLevelForm(forms.ModelForm):
  class Meta:
    model = Inventory
    fields = ['reorder_level']
    widgets = {
      'reorder_level' : forms.TextInput(attrs = {'class':'form-control input-height'}),
      
    }
    
  




