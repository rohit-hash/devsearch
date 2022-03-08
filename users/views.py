from atexit import register
from multiprocessing import context
from pdb import post_mortem
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.

def profiles(request):
    return render(request,'users/profiles.html')


def loginUser(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('profiles')



    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       try:
        user = User.objects.get(username=username)
       except:
         messages.error(request, "Username does not exist")
        
       user = authenticate(request, username=username, password=password )

       if user is not None:
        login(request,user)
        return redirect(profiles)
       else:
        messages.error(request,'Username or Password is incorrect')
       

    return render(request, 'users/login_register.html')

def logoutUser(request):
   logout(request)
   messages.error(request, "User was logged out")
   return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'User account was created!' )

            login(request,user)
            return redirect(profiles)
        else:
            messages.success(request,'An error has occurred during registration')
          
    context = {'page':page,'form':form}
    return render(request,'users/login_register.html',context) 
