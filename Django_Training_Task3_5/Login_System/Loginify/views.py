from enum import auto
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

from .forms import CreateUserForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from .models import UserDetails
from .serializer import UserDetail_Serializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login

# Create your views here.
def print_hello(request):
    return HttpResponse("hello I am django first view")

def signup_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():


            form.save()
              # Automatically log the user in after registration
            return redirect("Login")  # Redirect to the login page after signup
    context = {'registerform':form}    
    
        
    return render(request, 'Loginify/Signup.html',context=context)




    
  

def login_page(request):
    form = LoginForm()
    if request.method =='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            
            username = request.POST.get ('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:

                auth.login(request,user)
                return redirect("Confirmation")
    context = {'login_form':form}

    return render(request,'Loginify/Login.html')

def confirmation_page(request):
    return render(request,'Loginify/Confirmation.html')

@csrf_exempt
def get_all_userdata(request):
    if request.method == 'GET':
        try:
            all_users= UserDetails.objects.all() #queryset
            serializer_data = UserDetail_Serializer(all_users,many=True)
            return JsonResponse(serializer_data.data, safe=False)
        except Exception as e:
            return JsonResponse({"error":str(e)})
    
@csrf_exempt
def single_user_data(request,username):
    if request.method == 'GET':
        try:
            user_data=UserDetails.objects.get(username=username)   
            serializer_data= UserDetail_Serializer(user_data)
            return JsonResponse(serializer_data.data, safe=False)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
    # if request.method == 'PATCH':
    #     try:
    #         user_data=UserDetails.objects.get(pk=pk)
    #         input_data=json.loads(request.body)
    #         serializer_data=UserDetail_Serializer(user_data,data=input_data,partial=True)
    #         if serializer_data.is_valid():
    #             serializer_data.save()
    #             return JsonResponse({"message":"Data Updated Successfully"},status=200)
    #         else:
    #             return JsonResponse(serializer_data.errors,status=400)
    #     except UserDetails.DoesNotExist:
    #         return JsonResponse({"error":"User not found"},status=404)

    
    if request.method == 'DELETE':
        try:
            user_data=UserDetails.objects.get(username=username)
            user_data.delete()
            return JsonResponse({"message":"Data deleted Successfully"},status=204)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)     