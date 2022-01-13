from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .forms import InventoryForm, PatientForm
from .models import Account, Department,  Inventory,  Payment,Patient, Treatment, Day




class InventoryAdmin(SimpleHistoryAdmin):
   list_display = ['product_name','company_name','company_contact','unit_prize','exp_date','quantity','reorder_level', 'receive_quantity', 'receive_by', 'issue_quantity', 'issue_to', 'issue_by', 'last_updated']
   form = InventoryForm
   list_filter = [ 'exp_date', 'date_created']
   search_fields = ['product_name','company_name']
   history_list_display = ('product_name', 'receive_quantity', 'receive_by','issue_quantity','issue_to','issue_by','last_updated')

class PatientAdmin(SimpleHistoryAdmin):
   list_display = ['patient_lastName','patient_firstName','patient_middleName','patient_age','patient_sex','birth_date']
   form = PatientForm
   list_filter = ['patient_lastName','patient_sex', 'date_created']
   search_fields = ['patient_lastName','patient_firstName','patient_middleName','patient_age','patient_sex']
   
class TreatmentInLineAdmin(admin.TabularInline):
   model = Treatment
   
class DepartmentAdmin(SimpleHistoryAdmin):
   inlines = [TreatmentInLineAdmin]

admin.site.register(Day)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Treatment,SimpleHistoryAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Payment,SimpleHistoryAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Account)


