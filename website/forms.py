from django import forms
from django.forms import ModelForm
from .models import *

class BookAppointmentForm(forms.ModelForm):
  class Meta:
    model = BookAppointment
    fields = '__all__'
    widgets = {
      'first_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':"First Name", 'required':True }),
      'last_name': forms.TextInput(attrs = {'class':'form-control' }),
      'phone': forms.TextInput(attrs = {'class':'form-control' }),
      'email': forms.TextInput(attrs = {'class':'form-control' }),
      'day' : forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control input-height-sm', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
      'time': forms.TextInput(attrs = {'class':'form-control' }),
      'service': forms.TextInput(attrs = {'class':'form-control' }),
      'message': forms.Textarea(attrs = {'class':'form-control' }),
    }
    
class VirtualConsultForm(forms.ModelForm):
  class Meta:
    model = VirtualConsult
    fields = [ 'first_name','last_name','full_face','close_up','phone','email','message','assigned' ]
    
class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = [ 'name','email','message' ]