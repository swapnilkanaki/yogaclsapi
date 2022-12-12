
from django.urls import path
from yogaplatform import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="register"), 
    path('addmisson/', views.Addmisson, name="addmisson"), 
    path('logout/', views.LogOut, name="logout"), 
]
