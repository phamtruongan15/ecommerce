from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import TokenGenerator, generate_token

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
            if User.objects.get(username=email):
                messages.info(request, "Password is not matching")
                # return HttpResponse('email already exist')
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        
        user=User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
        email_subject = " activate Your Account"
        message = render_to_string('activate.html', {
            'user':user,
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
            
        })

        
        return HttpResponse("User created",email)    
                  
    print("hello is fuction ")
    return render(request,"signup.html")

def handlelogin(request):
    return render(request,"login.html")

def handlelogout(request):
    return redirect('/auther/login')