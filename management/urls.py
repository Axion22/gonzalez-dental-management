from django.urls import path
from . import views
from .views import ManageAppointmentTemplateView, virtualConsultationTemplateView, virtualConsultListView, ManageAppointmentStaffTemplateView, virtualConsultationStaff, paymentEditView
from django.contrib.auth import views as auth_views

urlpatterns = [

    #Administrator
    path('', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),

    path('dashboard-admin/', views.dashboardAdmin, name='dashboardAdmin'),

    path('department/', views.department, name='department'),
    path('department-create/', views.departmentAdd, name='departmentAdd'),
    path('department-edit/<int:id>/', views.departmentEdit, name='departmentEdit'),
    path('department-history/', views.departmentHistory, name='departmentHistory'),

    
    path('treatment-create/', views.departmentCreate, name='departmentCreate'),
    path('department-update/<int:id>/', views.treatmentCreate, name='treatmentCreate'),
    path('treatment-create-form/', views.treatmentCreateForm, name='treatmentCreateForm'),
    path('treatment-detail-form/<int:id>/', views.treatmentDetailForm, name='treatmentDetailForm'),
    path('treatment-delete-form/<int:id>', views.treatmentDeleteForm, name='treatmentDeleteForm'),
    path('treatment-update-form/<int:id>', views.treatmentUpdateForm, name='treatmentUpdateForm'),
    
 
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path('manage-appointments-assign/<int:id>/', views.assignDoctorAppointment, name='appointDoctor'),
    path('manage-appointments-table/', views.BookAppointmentTable, name='BookAppointmentTable'),
    path('manage-appointments-information/<int:id>', views.BookAppointmentInfo, name='BookAppointmentInfo'),
    path('manage-appointments-create/', views.appointmentCreate, name='BookAppointmentCreate'),
    
    path('virtual-consultation/', virtualConsultationTemplateView.as_view(), name='virtualConsultations'),
    path('virtual-consultation-assign/<int:id>/', views.assignDoctorVirtualConsult, name='assignDoctorVC'),


    

    path('doctor/', views.doctor, name='doctor'),
    path('register-doctor/', views.registerDoctor, name='registerDoctor'),
    
    path('staff/', views.staff, name='staff'),
    path('register-staff/', views.registerStaff, name='registerStaff'),

    path('patient/', views.patient, name='patient'),
    path('patient-create/', views.patientCreate, name='patientCreate'),
    path('patient-edit/<int:id>/', views.patientEdit, name='patientEdit'),
    path('patient-information/<int:id>/', views.patientInfo, name='patientInfo'),

    path('payment/', views.payment, name='payment'),
    path('payment-create/', views.paymentCreate, name='paymentCreate'),
    path('payment-edit/<int:id>/', views.paymentEdit, name='paymentEdit'),
    path('payment-edit/<int:id>/', paymentEditView.as_view(), name='paymentEditView'),
    path('payment-history/', views.paymentHistory, name='paymentHistory'),
    path('ajax/load-treatment/', views.load_treatment, name='ajax_load_treatment'),
    
    # Treatment Fee not Working
    path('ajax/load-treatment-fee/', views.load_treatment_fee, name='ajax_treatment_fee'),
    
    

    path('inventory/', views.inventory, name='inventory'),
    path('inventory-manage/<int:id>/', views.inventoryManage, name='inventoryManage'),
    path('inventory-issue/<int:id>/', views.inventoryIssue, name='inventoryIssue'),
    path('inventory-receive/<int:id>/', views.inventoryReceive, name='inventoryReceive'),
    path('inventory-create/', views.inventoryCreate, name='inventoryCreate'),
    path('inventory-edit/<int:id>/', views.inventoryEdit, name='inventoryEdit'),
    path('inventory-reorder-level/<str:pk>/', views.reorder_level, name="reorder_level"),
    

    path('account/', views.account, name='account'),
    path('account-edit/<int:id>/', views.accountEdit, name='accountEdit'),


    #Doctor
    path('dashboard-doctor/', views.dashboardDoctor, name='dashboardDoctor'),
    path('profile-doctor/', views.profileDoctor, name='profileDoctor'),
    path('profile-edit/', views.profileDoctorEdit, name='profileDoctorEdit'),
    

    path('appointment-doctor/', views.appointmentDoctor, name='appointmentDoctor'),
    path('appointment-delete-doctor/<int:id>/', views.appointmentDeleteDoctor, name='appointmentDeleteDoctor'),
    path('appointment-information-doctor/<int:id>/', views.BookAppointmentInfoDoctor, name='BookAppointmentInfoDoctor'),
    path('virtual-consultation-assigns/', virtualConsultListView.as_view(), name='virtualConsultationAssign'),
    





    path('patient-doctor/', views.patientDoctor, name='patientDoctor'),
    path('patient-create-doctor/', views.patientCreateDoctor, name='patientCreateDoctor'),
    path('patient-edit-doctor/<int:id>/', views.patientEditDoctor, name='patientEditDoctor'),
    path('patient-information-doctor/<int:id>/', views.patientInfoDoctor, name='patientInfoDoctor'),

    path('payment-doctor/', views.paymentDoctor, name='paymentDoctor'),
    path('payment-create-doctor/', views.paymentCreateDoctor, name='paymentCreateDoctor'),
    path('payment-edit-doctor/<int:id>/', views.paymentEditDoctor, name='paymentEditDoctor'),




    #Staff
    path('dashboard-staff/', views.dashboardStaff, name='dashboardStaff'),
    path('profile-staff/', views.profileStaff, name='profileStaff'),
    path('profile-staff-edit/', views.profileStaffEdit, name='profileStaffEdit'),
    
    
    
    path('appointments-staff/', ManageAppointmentStaffTemplateView.as_view(), name='appointmentStaff'),
    path('appointments-assign-staff/<int:id>/', views.assignDoctorStaffAppointment, name='appointDoctorStaff'),
    path('appointments-table-staff/', views.BookAppointmentTableStaff, name='BookAppointmentTableStaff'),
    path('appointments-information-staff/<int:id>/', views.BookAppointmentInfoStaff, name='BookAppointmentInfoStaff'),
    path('manage-appointments-create-staff/', views.appointmentCreateStaff, name='BookAppointmentCreateStaff'),

    
    path("virtual-consultation-staff/", virtualConsultationStaff.as_view(), name="virtualConsultationsStaff"),
    path('virtual-consultation-assign-staff/<int:id>/', views.assignStaffVirtualConsult, name='assignStaffVC'),
    
    
    path('doctor-staff/', views.doctorStaff, name='doctorStaff'),
    
    
    path('patient-staff/', views.patientStaff, name='patientStaff'),
    path('patient-create-staff/', views.patientCreateStaff, name='patientCreateStaff'),
    path('patient-edit-staff/<int:id>/', views.patientEditStaff, name='patientEditStaff'),
    path('patient-information-staff/<int:id>/', views.patientInfoStaff, name='patientInfoStaff'),
    
    
    path('payment-staff/', views.paymentStaff, name='paymentStaff'),
    path('payment-create-staff/', views.paymentCreateStaff, name='paymentCreateStaff'),
    path('payment-edit-staff/<int:id>/', views.paymentEditStaff, name='paymentEditStaff'),
    
    
    path('inventory-staff/', views.inventoryStaff, name='inventoryStaff'),
    path('inventory-manage-staff/<int:id>/', views.inventoryManageStaff, name='inventoryManageStaff'),
    path('inventory-issue-staff/<int:id>/', views.inventoryIssueStaff, name='inventoryIssueStaff'),
    path('inventory-receive-staff/<int:id>/', views.inventoryReceiveStaff, name='inventoryReceiveStaff'),
    path('inventory-create-staff/', views.inventoryCreateStaff, name='inventoryCreateStaff'),
    path('inventory-edit-staff/<int:id>/', views.inventoryEditStaff, name='inventoryEditStaff'),
    path('inventory-reorder-level-staff/<str:pk>/', views.reorder_levelStaff, name="reorder_levelStaff"),



]
