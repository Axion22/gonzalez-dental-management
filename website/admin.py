from django.contrib import admin
from .forms import BookAppointmentForm
from .models import BookAppointment, VirtualConsult, Contact

class BookAppointmentAdmin(admin.ModelAdmin):
   list_display = ['first_name','last_name','your_email','service_required', 'approved_date', 'approved_time', 'assign_doctor', 'accepted','accepted_date','done']
   form = BookAppointmentForm
   list_filter = ['first_name', 'last_name']
   search_fields = ['first_name', 'last_name']
   
class VirtualConsultAdmin(admin.ModelAdmin):
   list_display = ['first_name','last_name','assign_doctor', 'assigned']
   
   
   
class ContactAdmin(admin.ModelAdmin):
   list_display = ['name','email','message','date_created']


admin.site.register(BookAppointment,BookAppointmentAdmin)
admin.site.register(VirtualConsult, VirtualConsultAdmin)
admin.site.register(Contact,ContactAdmin)

