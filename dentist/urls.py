from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('website.urls')),
    path('', include('management.urls')),
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'management.views.error_404_view'


admin.site.site_header = "Gonzalez Dental Clinic - Admin"
admin.site.site_title = "Gonzalez Dental Clinic"
admin.site.index_title = "Superuser Site "