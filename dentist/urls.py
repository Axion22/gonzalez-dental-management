from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('management.urls')),
    path('home/', include('website.urls')),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)