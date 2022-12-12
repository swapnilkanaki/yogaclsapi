
from django.urls import path
from admissionapi import views

urlpatterns = [
    path('userloginapi/', views.UserLoginAPI),
    path('userregisterapi/', views.UserRegisterAPI),
    path('admissionapi/<int:id>', views.AdmissionAPI),
    path('completepaymentapi/<int:id>/<str:date>', views.CompletePaymentAPI),
    
]
