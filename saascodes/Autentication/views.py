from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
# Create your views here.
def login_page(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        myuser=authenticate(username=uname,password=password)
        
        if myuser is not None:
            login(request,myuser)
            return(render(request,'static/home_page.html',{'uname':uname}))
            #return(redirect('home_page',{'uname':uname}))
        
        
        else:
            return(redirect('signup_page'))

            
    return(render(request,'static/login_page.html'))

# def singup_page(request):
#     if request.method=='POST':
#         uname=request.POST['uname']
#         email=request.POST['email']
#         password=request.POST['password']

#         myuser=User.objects.create_user(uname,email,password)
#         myuser.save()
#         return(redirect('login_page'))
#     return(render(request,'static/signup_page.html'))




def signup_page(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']

        # Check if user already exists
        if User.objects.filter(username=uname).exists():
            return render(request, 'static/signup_page.html', {
                'error': 'Username already exists. Please choose another.'
            })

        try:
            myuser = User.objects.create_user(username=uname, email=email, password=password)
            myuser.save()
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login_page')
        except IntegrityError as e:
            messages.error(request, "Something went wrong. Please try again.")
            return render(request, 'static/signup_page.html', {
                'error': f"Failed to create user: {str(e)}"
            })

    return render(request, 'static/signup_page.html')
