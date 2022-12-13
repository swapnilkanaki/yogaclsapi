from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from admissionapi.models import User,Batches
from rest_framework import serializers
from admissionapi.serializers import UserSerializer,BatchesSerializer
from django.views.decorators.csrf import csrf_exempt

# Common Function To Get All Data From database
def getAllData(request,Table,TableSerializer):
        context={"msg":""}
        try:
            allData=Table.objects.all()
            serializer = TableSerializer(allData,many=True)
            return Response(serializer.data)
        except:
            context["msg"]="Data Not Found"
            return Response(context)


# API of userloginapi
@api_view(['POST','GET'])
@csrf_exempt
def UserLoginAPI(request):
    context={"msg":"","status":True,"id":None}
    
    if request.method == 'GET':
        return getAllData(request=request,Table=User,TableSerializer=UserSerializer)

    if request.method == 'POST':
            username = request.data.get("email")
            if User.objects.filter(email=username):
                user=User.objects.get(email=username)
                if request.data.get("password") != user.password:
                    context["status"]=False
                    context["id"]=user.id
                    context["msg"]=" UserId or Password Not Match "
                    return Response(context)
                else:
                    context["msg"]=" User Authanticated Successfully "
                    return Response(context)
            else:
                context["status"]=False
                context["msg"]=" UserId or Password Not Match "
                return Response(context)


# API of userregisterapi
@api_view(['GET','POST'])
@csrf_exempt
def UserRegisterAPI(request):
    
    if request.method == 'GET':
        return getAllData(request=request,Table=User,TableSerializer=UserSerializer)
    
    if request.method == 'POST':
        context={"msg":"","status":True,"id":None}
        serializer = UserSerializer(data = request.data)
        # try:
        if serializer.is_valid():
            serializer.save()
            context["msg"]=" User Registared Successful "
            return Response(context)
        # ecept:
        context["msg"]=" Enter Valid Data "
        context["status"]=False
        print("except / UserRegisterAPI- ",context)
        return Response(serializer.errors)

# API of admissionapi<int>
@api_view(['GET','POST'])
@csrf_exempt
def AdmissionAPI(request,id):
    
    if request.method == 'GET':
        context={"msg":"","status":True,"id":None}
        try:
            allData=Batches.objects.filter(batches_id=id)
            serializer = BatchesSerializer(allData,many=True)
            return Response(serializer.data)
        except:
            context["msg"]=" Data Not Found "
            context["status"]=False
            return Response(context)

    if request.method == 'POST':
        context={"msg":"","status":True,"id":None}
        serializer = BatchesSerializer(data = request.data)
        print(request.data)
        month=request.data['date'][:-2]
        if not Batches.objects.filter(batches_id=id,date__startswith=month):
            if serializer.is_valid():
                serializer.save()
                context["msg"]=" Batch Registared Successful "
                return Response(context)
        else:
            context["status"]=False
            context["msg"]=" Batch Allrady Selected "
            return Response(context)
        # return Response(serializers.errors)

# API of completepaymentapi/<int>/<str>
@api_view(['GET','POST'])
@csrf_exempt
def CompletePaymentAPI(request,id,date):
    context={"msg":"","status":True,"id":None}
    
    data = Batches.objects.filter(batches_id=id,date=date)
    print(data)
    serializer = BatchesSerializer(data = data)
    print(data)
    if serializer.is_valid():
        serializer.save()
        context["msg"]=" Payed Successful "
        return Response(context)
    else:
        context["status"]=False
        context["msg"]=" Allrady Payed "
        return Response(context)

