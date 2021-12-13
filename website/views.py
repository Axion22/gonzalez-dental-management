from django import template
from django.core.validators import EmailValidator
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from management.models import Department, Treatment
from django.template.loader import render_to_string
from management.views import department
from .forms import *

def home(request):
  department = Department.objects.filter(id=1)
  department = Department.objects.exclude(department='Staff')
  treatment = Treatment.objects.all()
  context = {
    'department':department,
    'treatment':treatment
  }
  return render(request, 'home.html', context)

def contact(request):
  if request.method == "POST":
    form = ContactForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
    message_name = request.POST['message-name']
    message_email = request.POST['message-email']
    message = request.POST['message']

    contact = Contact.objects.create(
      name = message_name,
      email = message_email,
      message = message,
    )
  



    template = render_to_string('emailc.html',{'name':message_name,'email':message_email,'message':message})
    email = EmailMessage(
      subject= f"{message_name} from Contact - Gonzalez Dental Clinic.",
      body=template,
      from_email= 'geraldlayderos202@gmail.com',
      to = ['axionultra@gmail.com','geraldlayderos202@gmail.com'],
    )
    email.send()
    

    return render(request,'contact.html',{
      'name': message_name,
      'email' : email,
      'message' : message,
      })
  else:
    return render(request,'contact.html',{})

def about(request):
  return render(request, 'about.html', {})

def pricing(request):
  department = Department.objects.all()
  department = Department.objects.exclude(department='Staff')
  treatment = Treatment.objects.all()
  context = {
    'department':department,
    'treatment':treatment
  }
  return render(request, 'pricing.html', context)

def service(request):
  department = Department.objects.all()
  department = Department.objects.exclude(department='Staff')
  form = VirtualConsultForm()
  if request.method == "POST":
    form = VirtualConsultForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      
    full_face= request.FILES['full-face']
    close_up = request.FILES['close-up']
    first_name = request.POST['first-name']
    last_name = request.POST['last-name']
    phone = request.POST['phone']
    email = request.POST['email']
    message =  request.POST['message']
    
    virtualconsult = VirtualConsult.objects.create(
      full_face = full_face,
      close_up = close_up,
      first_name = first_name,
      last_name = last_name,
      phone = phone,
      email = email,
      message = message
    )


    template = render_to_string('emailvc.html',{'fname':first_name,'lname':last_name, 'email':email,'message':message})
    email = EmailMessage(
      subject= f"{first_name} {last_name} from Virtual Consultation - Gonzalez Dental Clinic.",
      body=template,
      from_email= 'geraldlayderos202@gmail.com',
      to = ['axionultra@gmail.com','geraldlayderos202@gmail.com'],
    )
    email.send()


    return render(request,'service.html',{
      'first_name' : first_name,
      'last_name' : last_name,
      'department' : department,

      })
  else:
    return render(request, 'service.html', {'department':department})
  
  
  

def appointment(request):
  form = BookAppointmentForm()
  if request.method == "POST":
    form = BookAppointmentForm(request.POST)
    if form.is_valid():
      form.save()
      
    first_name = request.POST['first-name']
    last_name = request.POST['last-name']
    your_phone = request.POST['your-phone']
    your_email = request.POST['your-email']
    service_required = request.POST['service-required']
    your_schedule = request.POST['your-schedule']
    your_date = request.POST['your-date']
    your_message =  request.POST['your-message']
    
    appointment = BookAppointment.objects.create(
      first_name = first_name,
      last_name = last_name,
      your_phone = your_phone,
      your_email = your_email,
      service_required = service_required,
      your_schedule = your_schedule,
      your_date = your_date,
      your_message = your_message
    )

    


    template = render_to_string('email.html',{'fname':first_name,'lname':last_name, 'email':your_email,'service_required':service_required,'your_schedule':your_schedule,'your_date':your_date,'your_phone':your_phone})
    email = EmailMessage(
      subject= f"{first_name} {last_name} from Appointment -  Gonzalez Dental Clinic.",
      body=template,
      from_email= 'geraldlayderos202@gmail.com',
      to = ['axionultra@gmail.com','geraldlayderos202@gmail.com'],
    )
    email.send()
    
    
    return render(request,'appointment.html',{
      'first_name' : first_name,
      'last_name' : last_name,
      'your_phone' : your_phone,
      'your_email' : your_email,
      'service_required' :service_required,
      'your_schedule' : your_schedule,
      'your_date' : your_date,
      'your_message' : your_message,
      'form':form
      })
  else:
    return render(request,'home.html',{})





def FAQs(request):
  return render(request, 'FAQs.html', {})