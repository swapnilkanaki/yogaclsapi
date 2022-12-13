from django.shortcuts import render, redirect
from .forms import LoginForm
from django.conf import settings as conf_set
from admissionapi.models import User,Batches
import requests
import json


# Create your views here.
domen="http://3.112.13.233/"


#Login View api Userd (userloginapi)
def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        pload = {
                'email': email,
                'password': password                      
                }
        responce = requests.post(domen+'userloginapi/',data = pload)
        temp=json.loads(str(responce.text))
        if temp.get("status"):    
            data = User.objects.get(email=email, password=password)     
            request.session['userid']=data.id
            request.session['username']=data.name
            return redirect('addmisson')
        else:
            return redirect('login')    
    else:
        context = {"loginForm":"loginForm"}    
        return render(request, 'login.html',context) 
   
#Register New User View api Userd (userregisterapi)
def register(request):
        if request.method == 'POST':
            email=request.POST.get('email')
            password=request.POST.get('password')
            pload = {
                    "name": request.POST.get('name'),
                    "age": request.POST.get('age'),
                    "email": email,
                    "mobile": request.POST.get('mobile'),
                    "password": password                        
                    }
            responce = requests.post(domen+'userregisterapi/',data = pload)
            temp=json.loads(str(responce.text))
            if temp.get("status"): 
                data = User.objects.get(email=email, password=password)
                request.session['userid']=data.id
                request.session['username']=data.name
                return redirect('addmisson')
            else:
                return redirect('register')
        else:
            context = {"loginForm":"loginForm"}    
            return render(request, 'register.html',context)


#Addmisson of Yoga Class View api Userd (admissionapi/<int>)
def Addmisson(request):
    if request.session.has_key('username'):
        user_id = request.session['userid']
        batches_data=Batches.objects.filter(batches_id=user_id)
        if request.method == 'POST':
            pload = {
                    "batches_id":user_id,
                    "batch": request.POST.get('batch'),
                    "date": request.POST.get('date'),
                    "fees": 500                   
                    }
            responce = requests.post(domen+'admissionapi/{}'.format(user_id),data = pload)
            temp=json.loads(str(responce.text))
            if temp.get("status"): 
                return redirect('addmisson')
            else:
                return redirect('addmisson')
        else:
            context={
                'user_id' : user_id,
                'user_name' : request.session['username'],
                'batches_data' : batches_data,
                }
            return render(request,'admission.html',context)
    else:
        return redirect('login') 
    
#Logout or End session View
def LogOut(request):
    try:
        del request.session['userid']
        del request.session['username']
        return redirect('login')
    except KeyError:
        return redirect("login")    
