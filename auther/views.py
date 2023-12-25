from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, "Password is not matching")
            return render(request,'signup.html')
        try:
            if User.objects.get(user=email):
                return HttpResponse('email already exist')
        except Exception as identifier:
            pass
        
        user=User.objects.create_user(email,email,password)
        user.save()
        return HttpResponse("User created",email)    
                  
    print("hello is fuction ")
    return render(request,"signup.html")

def handlelogin(request):
    return render(request,"/login.html")

def handlelogout(request):
    return redirect('/auther/login')