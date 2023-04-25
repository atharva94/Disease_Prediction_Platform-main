from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Feedback
from accounts.forms import *
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(name,phone_number,email,message)
        try:
            Feedback_Form=Feedback(name=name,phone_number=phone_number,email=email,message=message)
            Feedback_Form.save()
            messages.success(request,"Feedback saved successfully")
        except Exception as e:
            messages.error(request,"Error occured!!!Fill the form again")
            print(e)
    return render(request,'index.html')


def Userlogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            print("User logged In")
            return redirect('dashboard')

        else:
            messages.error(request,"Username or Password is Incorrect")

    return render(request,"login.html")


def UserRegistration(request):
    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Successfuly created")
            return redirect("login")
        else:
            messages.error(request,"refill")
    context={
        "RegistrationForm":form
    }
    return render(request,"register.html",context)


