from pdb import post_mortem
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def profiles(request):
    return render(request,'users/profiles.html')


def loginUser(request):
    
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
