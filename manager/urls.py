from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [  
    url(r'^', include('authentication.urls')),
    url(r'employee/', include('employee.urls')),
    url(r'inventory/', include('inventory.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)