
from django.contrib import admin
from django.urls import path,include
# from admissionapi import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',include('admissionapi.urls')),
    path('',include('yogaplatform.urls')),
    
  
]
