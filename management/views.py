from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.views.generic import ListView, UpdateView
from website.models import BookAppointment, VirtualConsult
from django.http.response import HttpResponseRedirect,  HttpResponse, HttpResponseNotAllowed
import datetime
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

from .models import *
from .forms import *
from .filters import *
from .decorators import *
from django.db.models import F




# Login
@unauthenticated_user
def loginView(request):
  if request.method == 'POST':
    username=request.POST.get('username')
    password=request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('dashboardAdmin')

    else:
      messages.info(request, 'Username or Password is incorrect')

  context = {
    
  }
  return render(request, 'login/login.html',context )

# Logout
def logoutView(request):
  logout(request)
  return redirect('login')



# Admin
# Admin - Dashboard
@login_required(login_url='login')
@admin_only
def dashboardAdmin(request):
  department = Department.objects.all()
  total_department = department.count()
  
  appointment = BookAppointment.objects.filter(assign_doctor=None)
  total_appointment = appointment.count()
  
  consult = VirtualConsult.objects.filter(assigned=False)
  total_consult = consult.count()
  
  doctor = User.objects.all()
  doctor = User.objects.filter(groups__name__in=['doctor'])
  total_doctor = doctor.count()
  
  staff = User.objects.all()
  staff = User.objects.filter(groups__name__in=['staff'])
  total_staff = staff.count()
  
  inventory = Inventory.objects.all()
  total_inventory = inventory.count()
  
  patient = Patient.objects.all()
  total_patient = patient.count()
  
  payment = Payment.objects.all()
  total_payment = payment.count()
  
  context={
    'total_department':total_department,
    'total_appointment':total_appointment,
    'total_consult':total_consult,
    'total_doctor':total_doctor,
    'total_staff':total_staff,
    'total_patient':total_patient,
    'total_payment':total_payment,
    'total_inventory':total_inventory,
    
    }
  return render(request, 'adminTemp/dashboardAdmin.html', context)






# Admin - Department
@login_required(login_url='login')
@admin_only
def department(request):
  department = Department.objects.all()
  treatment = Treatment.objects.all()
  context = {
    'department':department,
    'treatment':treatment
  }
  return render(request, 'adminTemp/department.html', context)

# Admin - Department
@login_required(login_url='login')
@admin_only
def departmentHistory(request):
  historydepartment = Department.history.all()
  historytreatment = Treatment.history.all()
  
  
  
  page = request.GET.get('page', 1)

  paginator = Paginator(historydepartment, 10)
  try:
      historydepartmentpage = paginator.page(page)
  except PageNotAnInteger:
      historydepartmentpage = paginator.page(1)
  except EmptyPage:
      historydepartmentpage = paginator.page(paginator.num_pages)
     
     
      
  page = request.GET.get('page', 1)

  paginator = Paginator(historytreatment, 10)
  try:
      historytreatmentpage = paginator.page(page)
  except PageNotAnInteger:
      historytreatmentpage = paginator.page(1)
  except EmptyPage:
      historytreatmentpage = paginator.page(paginator.num_pages)
      
  context = {
    'historytreatmentpage':historytreatmentpage,
    'historydepartmentpage':historydepartmentpage

  }
  return render(request, 'adminTemp/departmentHistory.html', context)




# Admin - Department Create
@login_required(login_url='login')
@admin_only
def departmentCreate(request):
  form = DepartmentForm()
  if request.method == 'POST':
    form = DepartmentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('department')
  context = {
    'form':form
  }
  return render(request, 'adminTemp/departmentForm.html', context)

# Admin - Department Create Treatment
@login_required(login_url='login')
@admin_only
def treatmentCreate(request, id):
  department = Department.objects.get(id=id)
  treatment = Treatment.objects.filter(department=department)
  form = TreatmentForm(request.POST or None)
  
  if request.method == 'POST':
    if form.is_valid():
      treatment = form.save(commit=False)
      treatment.department = department
      treatment.save()
      return redirect('treatmentDetailForm', id=treatment.id)
    else:
      return render(request, 'adminTemp/partials/treatmentForm.html', {'form':form})
  context = {
    'form':form,
    'department':department,
    'treatment':treatment
  }
  return render(request, 'adminTemp/departmentForm.html', context)


# Admin - Department Create Treatment Form
@login_required(login_url='login')
@admin_only
def treatmentCreateForm(request):
  context = {
    "form": TreatmentForm()
  }
  return render(request, 'adminTemp/partials/treatmentForm.html', context)

# Admin - Department Detail Treatment Form
@login_required(login_url='login')
@admin_only
def treatmentDetailForm(request, id):
  treatment = Treatment.objects.get(id=id)
  context = {
    "treatment": treatment
  }
  return render(request, 'adminTemp/partials/treatmentDetailForm.html', context)


# Admin - Department Detail Delete Treatment Form
@login_required(login_url='login')
@admin_only
def treatmentDeleteForm(request, id):
  treatment = Treatment.objects.get(id=id)
  if request.method == "POST":
    treatment.delete()
    return HttpResponse('')
  
  return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


# Admin - Department Update Treatment Form
@login_required(login_url='login')
@admin_only
def treatmentUpdateForm(request, id):
  treatment = Treatment.objects.get(id=id)
  form = TreatmentForm(request.POST or None, instance=treatment)
  

  if request.method == "POST":
    if form.is_valid():
      form.save()
      return redirect("treatmentDetailForm", id=treatment.id)
    
  context = {
    "form": form,
    'treatment':treatment
  }
  return render(request, 'adminTemp/partials/treatmentForm.html', context)

 # Admin - Department Edit

@login_required(login_url='login')
@admin_only
def departmentEdit(request, id):
  departmentEdit = Department.objects.get(id=id)
  form = DepartmentForm(request.POST or None,instance=departmentEdit)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      return redirect("department")
  context = {
    'departmentEdit':departmentEdit,
    'form':form
  }
  
  return render(request, 'adminTemp/departmentEdit.html',context) 



 # Admin - Department Create

@login_required(login_url='login')
@admin_only
def departmentAdd(request):
  form = DepartmentForm()

  if request.method == 'POST':
    form = DepartmentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("department")
  context = {
    'form':form
  }
  
  return render(request, 'adminTemp/departmentAdd.html',context) 




# Admin - Appointment
    

# Admin - Appointment List
@method_decorator(login_required, name='dispatch')
@method_decorator(admin_only, name='dispatch')
class ManageAppointmentTemplateView(ListView):
    template_name = "adminTemp/bookAppointment.html"
    model = BookAppointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3
    
    
    
    
    def post(self, request):
      if 'accept' in self.request.POST:
        appointment_id = request.POST.get("appointment-id")
        appointment = BookAppointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.approved_date = appointment.your_date
        appointment.approved_time = appointment.your_schedule
        appointment.save()
          
        data = {
            "fname":appointment.first_name,
            "date":appointment.your_date,
            "time":appointment.your_schedule,
        }
          
        message = get_template('adminTemp/email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            'geraldlayderos202@gmail.com',
            [appointment.your_email],
        )
        email.content_subtype = "html"
        #email.send()
        
        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name} {appointment.last_name}")
        return HttpResponseRedirect(request.path)
        
      else:
        
        date = request.POST.get("date")
        time = request.POST.get("time")
        appointment_id = request.POST.get("appointment-id")
        appointment = BookAppointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.approved_date = date
        appointment.approved_time = time
        appointment.save()
            
        data = {
            "fname":appointment.first_name,
            "date":date,
            "time":time,
        }

        message = get_template('adminTemp/email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            'geraldlayderos202@gmail.com',
            [appointment.your_email],
        )
        email.content_subtype = "html"
        #email.send()


        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name} {appointment.last_name}")
        return HttpResponseRedirect(request.path)
      
      
    

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = BookAppointment.objects.all()
        context.update({   
          
        })
        return context

 
# Admin - Book Appointment Table
def BookAppointmentTable(request):
  context = {}
  
  filter_appointment = BookAppointmentFilter(request.GET, queryset= BookAppointment.objects.all())
  context['filter_appointment'] = filter_appointment
  
  paginated_appointment = Paginator(filter_appointment.qs ,10)
  page_number = request.GET.get('page')
  appointment_page = paginated_appointment.get_page(page_number)
  
  context['appointment_page'] = appointment_page
  
  
  return render(request, 'adminTemp/bookAppointmentTable.html', context=context)

    
    

# Admin - Book Appointment Assign Doctor
    
def assignDoctorAppointment(request, id):
  assignDoctor = BookAppointment.objects.get(id=id)
  form = BookAppointmentForm(instance=assignDoctor)
  
  if request.method == 'POST':
    form = BookAppointmentForm(request.POST, instance=assignDoctor)
    assignDoctor.is_deleted = True
    if form.is_valid():
      form.save()
      return redirect('manage')
  context = {
    'assignDoctor':assignDoctor,
    'form':form
  }
  
  
  return render(request, 'adminTemp/bookAppointmentDoctor.html', context)





# Admin - virtual Consultation
@method_decorator(login_required, name='dispatch')
@method_decorator(admin_only, name='dispatch')
class virtualConsultationTemplateView(ListView):
    template_name = "adminTemp/virtualConsultation.html"
    model = VirtualConsult
    context_object_name = "virtualconsultation"
    login_required = True
    paginate_by = 3
    
    
    def post(self, request):
        virtualconsult_id = request.POST.get("virtualconsult-id")
        virtualconsult = VirtualConsult.objects.get(id=virtualconsult_id)
        virtualconsult.accepted = True
        virtualconsult.accepted_date = datetime.datetime.now()
        virtualconsult.save()
        
        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {virtualconsult.first_name} {virtualconsult.last_name}")
        return HttpResponseRedirect(request.path)
      

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        virtualconsults = VirtualConsult.objects.all()
        context.update({   
          
        })
        return context
   

# Admin - virtual Consultation Assign Doctor
@login_required(login_url='login')
@admin_only     
def assignDoctorVirtualConsult(request, id):
  assignDoctorVC = VirtualConsult.objects.get(id=id)
  form = VirtualConsultationForm(instance=assignDoctorVC)
  
  if request.method == "POST":
    form = VirtualConsultationForm(request.POST, instance=assignDoctorVC)
    
    if form.is_valid():
      assignDoctorVC.assigned = True
      assignDoctorVC.save()
      form.save()
      
      return redirect('virtualConsultations')
  context = {
    'assignDoctorVC':assignDoctorVC,
    'form':form
  }
  
  
  return render(request, 'adminTemp/virtualConsultationAssign.html', context)   





# Admin - Contact to be
@method_decorator(login_required, name='dispatch')
@method_decorator(admin_only, name='dispatch')
class ContactTemplateView(ListView):
    template_name = 'adminTemp/contact.html'
    model = Contact
    context_object_name = "contact"
    login_required = True
    paginate_by = 3
    
    
    def post(self, request):
        message = request.POST.get("my_message")
        contact_id = request.POST.get("contact-id")
        contact = Contact.objects.get(id=contact_id)
        contact.accepted = True
        contact.accepted_date = datetime.datetime.now()
        contact.my_message = message

        contact.save()
        
        
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        contact = Contact.objects.all()
        context.update({   
          
        })
        return context
      
      
# Admin - Contact Assign

@login_required(login_url='login')
@admin_only
def contactForm(request,id):
  assignContact = Contact.objects.get(id=id)
  form = ContactForm(instance=assignContact)
  
  if request.method == "POST":
    form = ContactForm(request.POST, instance=assignContact)
    
    if form.is_valid():
      assignContact.assigned = True
      assignContact.save()
      form.save()
      
      return redirect('contacts')
  context = {
    'assignDoctorContact':assignContact,
    'form':form
  }
  
  
  return render(request, 'adminTemp/contactForm.html', context)

# Admin - Doctor


# Admin - Doctor List
@login_required(login_url='login')
@admin_only
def doctor(request):
  doctor = User.objects.all()
  doctor = User.objects.filter(groups__name__in=['doctor'])
  context = {
    'doctor':doctor
  }
  return render(request, 'adminTemp/doctor.html', context)


# Admin - Doctor Add

@login_required(login_url='login')
@admin_only
def registerDoctor(request):
  form = CreateUserForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      group = Group.objects.get(name = 'doctor')
      user.groups.add(group)
      Account.objects.create(user=user)
      messages.success(request, 'The DoctorAccount is Successfuly Created for ' + username)
      form = CreateUserForm()

  context = {
    'form':form
  }
  return render(request, 'adminTemp/registerDoctor.html', context)


# Admin - Staff

# Admin - Staff List
@login_required(login_url='login')
@admin_only
def staff(request):
  staff = User.objects.all()
  staff = User.objects.filter(groups__name__in=['staff'])
  context = {
    'staff':staff
  }
  return render(request, 'adminTemp/staff.html', context)

# Admin - Staff Add
@login_required(login_url='login')
@admin_only
def registerStaff(request):
  form = CreateUserForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      group = Group.objects.get(name = 'staff')
      user.groups.add(group)
      Account.objects.create(user=user)
      messages.success(request, 'The Staff Account is Successfuly Created for ' + username)
      form = CreateUserForm()

  context = {
    'form':form
  }
  return render(request, 'adminTemp/registerStaff.html', context)

# Admin - Patient



# Admin - Patient List

@login_required(login_url='login')
@admin_only
def patient(request):
  context = {}
  
  filter_patient = PatientFilter(request.GET, queryset= Patient.objects.all())
  context['filter_patient'] = filter_patient
  
  paginated_patient = Paginator(filter_patient.qs ,10)
  page_number = request.GET.get('page')
  patient_page = paginated_patient.get_page(page_number)
  
  context['patient_page'] = patient_page
  
  
  
  return render(request, 'adminTemp/patient.html',context=context)


# Admin - Patient Information

@login_required(login_url='login')
@admin_only
def patientInfo(request,id):
  patientInfo = Patient.objects.get(id=id)
  patientPayment = Payment.objects.filter(patient_name=patientInfo)
  
  context={
    'patientInfo':patientInfo,
    'patientPayment':patientPayment
  }
  return render(request, 'adminTemp/patientInfo.html',context)


# Admin - Patient Create

@login_required(login_url='login')
@admin_only
def patientCreate(request):
  form = PatientForm()
  if request.method == 'POST':
    form = PatientForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('patient')


  context = {
    'form':form
  }
  return render(request, 'adminTemp/patientForm.html',context)


# Admin - Patient Edit

@login_required(login_url='login')
@admin_only
def patientEdit(request, id):
  patientEdit = Patient.objects.get(id=id)
  form = PatientForm(instance=patientEdit)

  if request.method == 'POST':
    form = PatientForm(request.POST, instance=patientEdit)
    if form.is_valid():
      form.save()
      return redirect('patient')
  context = {
    'patientEdit':patientEdit,
    'form':form
  }
  
  return render(request, 'adminTemp/patientForm.html',context)


# Admin - Payment
 


# # Admin - Payment List

@login_required(login_url='login')
@admin_only
def payment(request):  
  context = {}
  
  filter_payment = PaymentFilter(request.GET, queryset= Payment.objects.all())
  context['filter_payment'] = filter_payment
  
  paginated_payment = Paginator(filter_payment.qs ,10)
  page_number = request.GET.get('page')
  payment_page = paginated_payment.get_page(page_number)
  
  context['payment_page'] = payment_page

  return render(request, 'adminTemp/payment.html', context=context)



# # Admin - Payment History
@login_required(login_url='login')
@admin_only
def paymentHistory(request): 
   
  historypayment = Payment.history.all()
  page = request.GET.get('page', 1)

  paginator = Paginator(historypayment, 10)
  try:
      paymentpage = paginator.page(page)
  except PageNotAnInteger:
      paymentpage = paginator.page(1)
  except EmptyPage:
      paymentpage = paginator.page(paginator.num_pages)
      
  context = {
    'historypayment':historypayment,
    'paymentpage':paymentpage
    }
  return render(request, 'adminTemp/paymentHistory.html', context)


# Admin - Payment Create

@login_required(login_url='login')
@admin_only
def paymentCreate(request):
  form = PaymentForm()
  if request.method == 'POST':
    form = PaymentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('payment')

  context = {
    'form':form
  }
  return render(request, 'adminTemp/paymentForm.html',context)


# Admin - Payment Edit
@method_decorator(login_required, name='dispatch')
@method_decorator(admin_only, name='dispatch')
class paymentEditView(UpdateView):
  model = Payment
  form_class = PaymentForm
  success_url = reverse_lazy('payment')
  

def load_treatment(request):
  department_id = request.GET.get('department')
  treatment = Treatment.objects.filter(department_id=department_id).order_by('treatment')
  return render(request, 'adminTemp/paymentTreatmentOptions.html', {'treatment':treatment})


  
def load_treatment_fee(request):
  treatment_id = request.GET.get('treatment')
  treatment = Treatment.objects.get(id=treatment_id)

  context = {
    'treatment':treatment
    }
  return render(request, 'adminTemp/paymentTreatmentFee.html',  context)
  
    



@login_required(login_url='login')
@admin_only
def paymentEdit(request, id):

  paymentEdit = Payment.objects.get(id=id)
  form = PaymentForm(instance=paymentEdit)

  if request.method == 'POST':
    form = PaymentForm(request.POST, instance=paymentEdit)
    if form.is_valid():
      form.save()
      return redirect('payment')

  context = {
    'paymentEdit':paymentEdit,
    'form':form,

  }
  
  return render(request, 'adminTemp/paymentForm.html',context)

  
  
  
# Admin - Inventory

# Admin - Inventory List

@login_required(login_url='login')
@admin_only
def inventory(request):
  
  context = {}
  
  filter_inventory = InventoryFilter(request.GET, queryset= Inventory.objects.all())
  context['filter_inventory'] = filter_inventory
  
  paginated_inventory = Paginator(filter_inventory.qs ,10)
  page_number = request.GET.get('page')
  inventory_page = paginated_inventory.get_page(page_number)
  
  context['inventory_page'] = inventory_page

  return render(request, 'adminTemp/inventory.html', context=context)


# Admin - Inventory Create

@login_required(login_url='login')
@admin_only
def inventoryCreate(request):
  form = InventoryForm()
  if request.method == 'POST':
    form = InventoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('inventory')


  context = {
    'form':form
  }
  return render(request, 'adminTemp/inventoryForm.html',context)




# Admin - Inventory Manage

@login_required(login_url='login')
@admin_only
def inventoryManage(request, id):
  inventoryManage = Inventory.objects.get(id=id)
  history = Inventory.history.filter(id=id)
  
  page = request.GET.get('page', 1)

  paginator = Paginator(history, 5)
  try:
      historypage = paginator.page(page)
  except PageNotAnInteger:
      historypage = paginator.page(1)
  except EmptyPage:
      historypage = paginator.page(paginator.num_pages)
  
  
  context = {
    'inventoryManage':inventoryManage,
    'historypage':historypage
    }
  return render(request, 'adminTemp/inventoryManage.html', context)




@login_required(login_url='login')
@admin_only
def inventoryIssue(request, id):
  inventoryIssue = Inventory.objects.get(id=id)
  form = InventoryIssueForm(request.POST or None, instance=inventoryIssue)
  if form.is_valid():
    instance = form.save(commit=False)
    if instance.issue_quantity > instance.quantity:
      messages.info(request, 'Exceed the number of Item')
      return redirect('/inventory-issue/'+str(instance.id))
    else:
      instance.quantity -= instance.issue_quantity
      instance.issue_by = str(request.user.get_full_name())
    messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.product_name) + "s now left in Inventory")

    instance.save()
    return redirect('/inventory-manage/'+str(instance.id))

  context = {
      "title": 'Issue ' + str(inventoryIssue.product_name),
      "inventoryIssue": inventoryIssue,
      "form": form,
      "username": 'Issue By: ' + str(request.user),
    }
  return render(request, 'adminTemp/inventoryIssue.html',context)


# Admin - Inventory Manage Receive

@login_required(login_url='login')
@admin_only
def inventoryReceive(request, id):
  inventoryReceive = Inventory.objects.get(id=id)
  form = InventoryReceiveForm(request.POST or None, instance=inventoryReceive)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.quantity += instance.receive_quantity
    messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.product_name) + "s now left in Inventory")

    instance.save()
    return redirect('/inventory-manage/'+str(instance.id))

  context = {
      "title": 'Receive ' + str(inventoryReceive.product_name),
      "inventoryReceive": inventoryReceive,
      "form": form,
      "username": 'Receive By: ' + str(request.user),
    }
  return render(request, 'adminTemp/inventoryReceive.html',context)



# Admin - Inventory Edit

@login_required(login_url='login')
@admin_only
def inventoryEdit(request, id):
  inventoryEdit = Inventory.objects.get(id=id)
  form = InventoryForm(instance=inventoryEdit)

  if request.method == 'POST':
    form = InventoryForm(request.POST, instance=inventoryEdit)
    if form.is_valid():
      form.save()
      messages.info(request, 'Successfully Updated')
      return redirect('inventory')
    
  context = {
    'inventoryEdit':inventoryEdit,
    'form':form
  }
  
  return render(request, 'adminTemp/inventoryForm.html',context)



# Admin - Inventory Reorder
@login_required(login_url='login')
@admin_only
def reorder_level(request, pk):
	reorderLevel = Inventory.objects.get(id=pk)
	form = ReorderLevelForm(request.POST or None, instance=reorderLevel)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.product_name) + " is updated to " + str(instance.reorder_level))

		return redirect("inventory")
	context = {
			"instance": reorderLevel,
			"form": form,
		}
	return render(request, "adminTemp/inventoryReorder.html", context)



##
@login_required(login_url='login')
@admin_only
def inventoryCreate(request):
  form = InventoryForm()
  if request.method == 'POST':
    form = InventoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('inventory')


  context = {
    'form':form
  }
  return render(request, 'adminTemp/inventoryForm.html',context)


# Admin - Account

# Admin - Account List
@login_required(login_url='login')
@admin_only
def account(request):
  user = User.objects.all()
  context = {
    'user':user
  }
  return render(request, 'adminTemp/account.html',context)


# Admin - Account Create
@login_required(login_url='login')
@admin_only
def accountCreate(request):
  form = CreateUserForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      group = Group.objects.get(name = 'admin')
      user.groups.add(group)
      messages.success(request, 'The DoctorAccount is Successfuly Created for ' + username)
      form = CreateUserForm()
  

  context = {
    'form':form
  }
  return render(request, 'adminTemp/accountForm.html',context)


# Admin - Account Edit
@login_required(login_url='login')
@admin_only
def accountEdit(request, id):
  user = User.objects.get(id=id)
  if request.method == 'POST':
    form = CreateUserForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      return redirect('account')
    
  else:
    form = CreateUserForm(instance=user)
  context = {
    'form':form
  }
  return render(request, 'adminTemp/accountForm.html',context)














# Staff
@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def dashboardStaff(request):
  doctor = User.objects.all() 
  doctor = User.objects.filter(groups__name__in=['doctor'])
  vr = VirtualConsult.objects.filter(assigned=False)
  ba = BookAppointment.objects.filter(assign_doctor=None)
  day1 = Account.objects.filter(schedule_day=1).exclude(department=5)
  day2 = Account.objects.filter(schedule_day=2).exclude(department=5)
  day3 = Account.objects.filter(schedule_day=3).exclude(department=5)
  day4 = Account.objects.filter(schedule_day=4).exclude(department=5)
  day5 = Account.objects.filter(schedule_day=5).exclude(department=5)
  day6 = Account.objects.filter(schedule_day=6).exclude(department=5)
  day7 = Account.objects.filter(schedule_day=7).exclude(department=5)
  
  inventory = Inventory.objects.filter(quantity__lte=F('reorder_level')) 
  payment = Payment.objects.filter(status = 'unpaid') 
  
  context = {
    'doctor':doctor,
    'vr':vr,
    'ba':ba,
    'day1':day1,
    'day2':day2,
    'day3':day3,
    'day4':day4,
    'day5':day5,
    'day6':day6,
    'day7':day7,
    'inventory':inventory,
    'payment':payment
  }
  return render(request, 'staffTemp/dashboardStaff.html', context)




# Staff - Profile Edit
@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def profileStaff(request):
  user = request.user.account

  context = {
    'user':user
  }
  return render(request, 'staffTemp/account.html', context)


# Staff - Profile Edit
@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def profileStaffEdit(request):
  user = request.user.account
  form = accountForm(instance=user)
  if request.method == 'POST':
    form = accountForm(request.POST, instance=user)
  if form.is_valid():
    obj = form.save(commit=False)
    obj.save()
    form.save_m2m()
    messages.success(request, 'Your Profile account is successfully updated ')
    
    return redirect('profileStaff')
    
  context = {
    'form':form
  }
  return render(request, 'staffTemp/accountForm.html', context)


# Staff - Appointment
    

# Staff - Appointment List
@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['staff']), name='dispatch')
class ManageAppointmentStaffTemplateView(ListView):
    template_name = "staffTemp/bookAppointment.html"
    model = BookAppointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3
    
    
    
    
    def post(self, request):
      if 'accept' in self.request.POST:
        appointment_id = request.POST.get("appointment-id")
        appointment = BookAppointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.approved_date = appointment.your_date
        appointment.approved_time = appointment.your_schedule
        appointment.save()
          
        data = {
            "fname":appointment.first_name,
            "date":appointment.your_date,
            "time":appointment.your_schedule,
        }
          
        message = get_template('adminTemp/email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            'geraldlayderos202@gmail.com',
            [appointment.your_email],
        )
        email.content_subtype = "html"
        #email.send()
        
        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name} {appointment.last_name}")
        return HttpResponseRedirect(request.path)
        
      else:
        
        date = request.POST.get("date")
        time = request.POST.get("time")
        appointment_id = request.POST.get("appointment-id")
        appointment = BookAppointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.approved_date = date
        appointment.approved_time = time
        appointment.save()
            
        data = {
            "fname":appointment.first_name,
            "date":date,
            "time":time,
        }

        message = get_template('adminTemp/email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            'geraldlayderos202@gmail.com',
            [appointment.your_email],
        )
        email.content_subtype = "html"
        #email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name} {appointment.last_name}")
        return HttpResponseRedirect(request.path)
      
      
    

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = BookAppointment.objects.all()
        context.update({   
          
        })
        return context
    
    

# Staff - Book Appointment Assign Doctor
@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def assignDoctorStaffAppointment(request, id):
  assignDoctor = BookAppointment.objects.get(id=id)
  form = BookAppointmentForm(instance=assignDoctor)
  
  if request.method == 'POST':
    form = BookAppointmentForm(request.POST, instance=assignDoctor)
    assignDoctor.is_deleted = True
    if form.is_valid():
      form.save()
      return redirect('manage')
  context = {
    'assignDoctor':assignDoctor,
    'form':form
  }
  
  
  return render(request, 'staffTemp/bookAppointmentDoctor.html', context)


# Staff - virtual Consultation
@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['staff']), name='dispatch')
class virtualConsultationStaff(ListView):
    template_name = "staffTemp/virtualConsultation.html"
    model = VirtualConsult
    context_object_name = "virtualconsultation"
    login_required = True
    paginate_by = 3
    
    
    def post(self, request):
        virtualconsult_id = request.POST.get("virtualconsult-id")
        virtualconsult = VirtualConsult.objects.get(id=virtualconsult_id)
        virtualconsult.accepted = True
        virtualconsult.accepted_date = datetime.datetime.now()
        virtualconsult.save()
        

      

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        virtualconsults = VirtualConsult.objects.all()
        context.update({   
          
        })
        return context
   

# Staff - virtual Consultation Assign Doctor
@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])    
def assignStaffVirtualConsult(request, id):
  assignDoctorVC = VirtualConsult.objects.get(id=id)
  form = VirtualConsultationForm(instance=assignDoctorVC)
  
  if request.method == "POST":
    form = VirtualConsultationForm(request.POST, instance=assignDoctorVC)
    
    if form.is_valid():
      assignDoctorVC.assigned = True
      assignDoctorVC.save()
      form.save()
      
      return redirect('virtualConsultationsStaff')
  context = {
    'assignDoctorVC':assignDoctorVC,
    'form':form
  }
  
  
  return render(request, 'staffTemp/virtualConsultationAssign.html', context) 



# Staff - Doctor List
@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def doctorStaff(request):
  doctor = User.objects.all()
  doctor = User.objects.filter(groups__name__in=['doctor'])
  day1 = Account.objects.filter(schedule_day=1).exclude(department=5)
  day2 = Account.objects.filter(schedule_day=2).exclude(department=5)
  day3 = Account.objects.filter(schedule_day=3).exclude(department=5)
  day4 = Account.objects.filter(schedule_day=4).exclude(department=5)
  day5 = Account.objects.filter(schedule_day=5).exclude(department=5)
  day6 = Account.objects.filter(schedule_day=6).exclude(department=5)
  day7 = Account.objects.filter(schedule_day=7).exclude(department=5)
  
  context = {
    'doctor':doctor,
    'day1':day1,
    'day2':day2,
    'day3':day3,
    'day4':day4,
    'day5':day5,
    'day6':day6,
    'day7':day7,
  }
  return render(request, 'staffTemp/doctor.html', context)





# Staff - Patient



# Staff - Patient List

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def patientStaff(request):
  context = {}
  
  filter_patient = PatientFilter(request.GET, queryset= Patient.objects.all())
  context['filter_patient'] = filter_patient
  
  paginated_patient = Paginator(filter_patient.qs ,10)
  page_number = request.GET.get('page')
  patient_page = paginated_patient.get_page(page_number)
  
  context['patient_page'] = patient_page
  
  
  
  return render(request, 'staffTemp/patient.html',context=context)


# Staff - Patient Information

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def patientInfoStaff(request,id):
  patientInfo = Patient.objects.get(id=id)
  patientPayment = Payment.objects.filter(patient_name=patientInfo)
  context={
    'patientInfo':patientInfo,
    'patientPayment':patientPayment
  }
  return render(request, 'staffTemp/patientInfo.html', context)



# Staff - Patient Create

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def patientCreateStaff(request):
  form = PatientForm()
  if request.method == 'POST':
    form = PatientForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('patient')


  context = {
    'form':form
  }
  return render(request, 'staffTemp/patientForm.html',context)


# Staff - Patient Edit

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def patientEditStaff(request, id):
  patientEdit = Patient.objects.get(id=id)
  form = PatientForm(instance=patientEdit)

  if request.method == 'POST':
    form = PatientForm(request.POST, instance=patientEdit)
    if form.is_valid():
      form.save()
      return redirect('patient')
  context = {
    'patientEdit':patientEdit,
    'form':form
  }
  
  return render(request, 'staffTemp/patientForm.html',context)





# Staff - Payment
 


# # Staff - Payment List

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def paymentStaff(request):  
  context = {}
  
  filter_payment = PaymentFilter(request.GET, queryset= Payment.objects.all())
  context['filter_payment'] = filter_payment
  
  paginated_payment = Paginator(filter_payment.qs ,10)
  page_number = request.GET.get('page')
  payment_page = paginated_payment.get_page(page_number)
  
  context['payment_page'] = payment_page

  return render(request, 'staffTemp/payment.html', context=context)


# Staff - Payment Create

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def paymentCreateStaff(request):
  form = PaymentForm()
  if request.method == 'POST':
    form = PaymentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('payment')

  context = {
    'form':form
  }
  return render(request, 'staffTemp/paymentForm.html',context)



# Staff - Payment Edit

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def paymentEditStaff(request, id):
  paymentEdit = Payment.objects.get(id=id)
  form = PaymentForm(instance=paymentEdit)

  if request.method == 'POST':
    form = PaymentForm(request.POST, instance=paymentEdit)
    if form.is_valid():
      form.save()
      return redirect('payment')

  context = {
    'paymentEdit':paymentEdit,
    'form':form,
  }
  
  return render(request, 'staffTemp/paymentForm.html',context)




# Staff - Inventory

# Staff - Inventory List

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def inventoryStaff(request):
  
  context = {}
  
  filter_inventory = InventoryFilter(request.GET, queryset= Inventory.objects.all())
  context['filter_inventory'] = filter_inventory
  
  paginated_inventory = Paginator(filter_inventory.qs ,10)
  page_number = request.GET.get('page')
  inventory_page = paginated_inventory.get_page(page_number)
  
  context['inventory_page'] = inventory_page

  return render(request, 'staffTemp/inventory.html', context=context)


# Admin - Inventory Create

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def inventoryCreateStaff(request):
  form = InventoryForm()
  if request.method == 'POST':
    form = InventoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('inventoryStaff')


  context = {
    'form':form
  }
  return render(request, 'staffTemp/inventoryForm.html',context)




# Staff - Inventory Manage

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def inventoryManageStaff(request, id):
  inventoryManage = Inventory.objects.get(id=id)
  history = Inventory.history.filter(id=id)
  
  page = request.GET.get('page', 1)

  paginator = Paginator(history, 10)
  try:
      historypage = paginator.page(page)
  except PageNotAnInteger:
      historypage = paginator.page(1)
  except EmptyPage:
      historypage = paginator.page(paginator.num_pages)
  
  
  context = {
    'inventoryManage':inventoryManage,
    'historypage':historypage
    }
  return render(request, 'staffTemp/inventoryManage.html', context)



# Staff - Inventory Issue

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def inventoryIssueStaff(request, id):
  inventoryIssue = Inventory.objects.get(id=id)
  form = InventoryIssueForm(request.POST or None, instance=inventoryIssue)
  if form.is_valid():
    instance = form.save(commit=False)
    if instance.issue_quantity > instance.quantity:
      messages.info(request, 'Exceed the number of Item')
      return redirect('/inventory-issue-staff/'+str(instance.id))
    else:
      instance.quantity -= instance.issue_quantity
      instance.issue_by = str(request.user.get_full_name())
    messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.product_name) + "s now left in Inventory")

    instance.save()
    return redirect('/inventory-manage-staff/'+str(instance.id))

  context = {
      "title": 'Issue ' + str(inventoryIssue.product_name),
      "inventoryIssue": inventoryIssue,
      "form": form,
      "username": 'Issue By: ' + str(request.user),
    }
  return render(request, 'staffTemp/inventoryIssue.html',context)


# Staff - Inventory Manage Receive

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def inventoryReceiveStaff(request, id):
  inventoryReceive = Inventory.objects.get(id=id)
  form = InventoryReceiveForm(request.POST or None, instance=inventoryReceive)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.quantity += instance.receive_quantity
    messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.product_name) + "s now left in Inventory")

    instance.save()
    return redirect('/inventory-manage-staff/'+str(instance.id))

  context = {
      "title": 'Receive ' + str(inventoryReceive.product_name),
      "inventoryReceive": inventoryReceive,
      "form": form,
      "username": 'Receive By: ' + str(request.user),
    }
  return render(request, 'staffTemp/inventoryReceive.html',context)



# Staff - Inventory Edit

@login_required(login_url='login')
def inventoryEditStaff(request, id):
  inventoryEdit = Inventory.objects.get(id=id)
  form = InventoryForm(instance=inventoryEdit)

  if request.method == 'POST':
    form = InventoryForm(request.POST, instance=inventoryEdit)
    if form.is_valid():
      form.save()
      messages.info(request, 'Successfully Updated')
      return redirect('inventoryStaff')
    
  context = {
    'inventoryEdit':inventoryEdit,
    'form':form
  }
  
  return render(request, 'staffTemp/inventoryForm.html',context)



# Staff - Inventory Reorder
@login_required(login_url='login')
@allowed_users(allowed_roles=['staff']) 
def reorder_levelStaff(request, pk):
	reorderLevel = Inventory.objects.get(id=pk)
	form = ReorderLevelForm(request.POST or None, instance=reorderLevel)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.product_name) + " is updated to " + str(instance.reorder_level))

		return redirect("inventoryStaff")
	context = {
			"instance": reorderLevel,
			"form": form,
		}
	return render(request, "staffTemp/inventoryReorder.html", context)








  















# Doctor

# Doctor - Dashboard
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def dashboardDoctor(request):
  
  vr = VirtualConsult.objects.filter(accepted=False, assign_doctor= request.user.account)
  ba = BookAppointment.objects.filter( is_deleted=False, assign_doctor= request.user.account)
  payment = Payment.objects.filter(status = 'unpaid' )
  
  context = {
    'vr':vr,
    'ba':ba,
    'payment':payment
  }
  return render(request, 'doctorTemp/dashboardDoctor.html', context)


# Doctor - Profile
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def profileDoctor(request):
  user = request.user.account

    
  context = {
    'user':user
  }
  return render(request, 'doctorTemp/account.html', context)

# Doctor - Profile Edit
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def profileDoctorEdit(request):
  user = request.user.account
  form = accountForm(instance=user)
  if request.method == 'POST':
    form = accountForm(request.POST, instance=user)
  if form.is_valid():
    obj = form.save(commit=False)
    obj.save()
    form.save_m2m()
    messages.success(request, 'Your Profile account is successfully updated ')
    
    return redirect('profileDoctor')
    
  context = {
    'form':form
  }
  return render(request, 'doctorTemp/accountForm.html', context)





# Doctor - Appointment

# Doctor - Appointment List
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def appointmentDoctor(request):
  users = request.user.account
  user = BookAppointment.objects.filter( assign_doctor=users, is_deleted=False ).order_by('-accepted_date')
  context = {
    'user':user
  }
  return render(request, 'doctorTemp/appointment.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def appointmentDeleteDoctor(request, id):
  appointmentDeleteDoctor = BookAppointment.objects.get(id=id)
  if request.method == "POST":
    appointmentDeleteDoctor.is_deleted = True
    appointmentDeleteDoctor.save()
    return redirect('appointmentDoctor')
  context = {
    'appoint':appointmentDeleteDoctor
  }
  return render(request, 'doctorTemp/appointmentDelete.html', context)





# Doctor - Book Appointment
@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['doctor']), name='dispatch') 
class virtualConsultListView(ListView):
    template_name = "doctorTemp/virtualConsultationDoctor.html"
    model = VirtualConsult
    context_object_name = "virtualconsultations"
    login_required = True
    paginate_by = 3


    def get_queryset(self):
        user = self.request.user.account
        return VirtualConsult.objects.filter(assign_doctor=user)
      
    def post(self, request):
        message = request.POST.get("my_message")
        virtualconsult_id = request.POST.get("virtualconsult-id")
        virtualconsult = VirtualConsult.objects.get(id=virtualconsult_id)
        virtualconsult.accepted = True
        virtualconsult.accepted_date = datetime.datetime.now()
        virtualconsult.my_message = message

        virtualconsult.save()
        
        
        data = {
            "fname":virtualconsult.first_name,
            "message":message,
        }

        message = get_template('doctorTemp/emailvirtualconsult.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            'geraldlayderos202@gmail.com',
            [virtualconsult.email],
        )
        email.content_subtype = "html"
        #email.send()


        messages.add_message(request, messages.SUCCESS, f"You accepted the virtual consult of {virtualconsult.first_name} {virtualconsult.last_name}")
        return HttpResponseRedirect(request.path)
      

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        virtualconsults = VirtualConsult.objects.all()
        context.update({   
          
        })
        return context
      
      
# Doctor - Virtual Consultation Assigned
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def assignedVirtualConsultation(request):
  
  return render(request, 'doctorTemp/virtualConsultationDoctor.html', {})
# Doctor - Patient


@login_required(login_url='login')
@admin_only
def patient(request):
  context = {}
  
  filter_patient = PatientFilter(request.GET, queryset= Patient.objects.all())
  context['filter_patient'] = filter_patient
  
  paginated_patient = Paginator(filter_patient.qs ,10)
  page_number = request.GET.get('page')
  patient_page = paginated_patient.get_page(page_number)
  
  context['patient_page'] = patient_page
  
  
  
  return render(request, 'adminTemp/patient.html',context=context)


# Doctor - Patient List
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def patientDoctor(request):
  
  context = {}
  
  filter_patient = PatientFilter(request.GET, queryset= Patient.objects.all())
  context['filter_patient'] = filter_patient
  
  paginated_patient = Paginator(filter_patient.qs ,10)
  page_number = request.GET.get('page')
  patient_page = paginated_patient.get_page(page_number)
  
  context['patient_page'] = patient_page
  
  return render(request, 'doctorTemp/patient.html', context)


# Doctor - Patient Create
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def patientCreateDoctor(request):
  form = PatientForm()
  if request.method == 'POST':
    form = PatientForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('patientDoctor')


  context = {
    'form':form
  }
  return render(request, 'doctorTemp/patientForm.html', context)


# Doctor - Patient Edit
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def patientEditDoctor(request, id):
  patientEdit = Patient.objects.get(id=id)
  form = PatientForm(instance=patientEdit)

  if request.method == 'POST':
    form = PatientForm(request.POST, instance=patientEdit)
    if form.is_valid():
      form.save()
      return redirect('patientDoctor')
  context = {
    'patientEdit':patientEdit,
    'form':form
  }
  return render(request, 'doctorTemp/patientForm.html', context)


# Doctor - Patient Information
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def patientInfoDoctor(request, id):
  patientInfo = Patient.objects.get(id=id)
  patientPayment = Payment.objects.filter(patient_name=patientInfo)
  
  context={
    'patientInfo':patientInfo,
    'patientPayment':patientPayment
  }
  return render(request, 'doctorTemp/patientInfo.html', context)



# Doctor - Payment

# Doctor - Payment List
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def paymentDoctor(request):
  context = {}
  
  filter_payment = PaymentFilter(request.GET, queryset= Payment.objects.all())
  context['filter_payment'] = filter_payment
  
  paginated_payment = Paginator(filter_payment.qs ,10)
  page_number = request.GET.get('page')
  payment_page = paginated_payment.get_page(page_number)
  
  context['payment_page'] = payment_page

  return render(request, 'doctorTemp/payment.html', context)


# Doctor - Payment Create
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def paymentCreateDoctor(request):
  form = PaymentForm()
  if request.method == 'POST':
    form = PaymentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('payment')

  context = {
    'form':form
  }
  return render(request, 'doctorTemp/paymentForm.html', context)




class paymentEditViewDoctor(UpdateView):
  model = Payment
  form_class = PaymentForm
  success_url = reverse_lazy('payment')
  

def load_treatment(request):
  department_id = request.GET.get('department')
  treatment = Treatment.objects.filter(department_id=department_id).order_by('treatment')
  return render(request, 'adminTemp/paymentTreatmentOptions.html', {'treatment':treatment})





# Doctor - Payment Edit
@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def paymentEditDoctor(request, id):
  paymentEdit = Payment.objects.get(id=id)
  form = PaymentForm(instance=paymentEdit)

  if request.method == 'POST':
    form = PaymentForm(request.POST, instance=paymentEdit)
    if form.is_valid():
      form.save()
      return redirect('paymentDoctor')
  context = {
    'paymentEdit':paymentEdit,
    'form':form
  }
  return render(request, 'doctorTemp/paymentForm.html', context)













