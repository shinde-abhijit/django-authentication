from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        passw = request.POST.get('passw')
        dob = request.POST.get('dob')
        if User.objects.filter(username=name).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'Username or email already exists. Please choose a different one.')
            return redirect('register-user')
        else:        
            new_user = User.objects.create_user(name, email, passw)
            new_user.first_name = fname
            new_user.last_name = lname
            new_user.save()
        return redirect('login-user')
    return render(request, 'authenticate/register_user.html')


def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        passw = request.POST.get('passw')

        user = authenticate(request, username=name, password=passw)
        
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            # Check if the username exists
            if not User.objects.filter(username=name).exists():
                messages.error(request, 'Username does not exist.')
            else:
                messages.error(request, 'Incorrect password.')

    return render(request, 'authenticate/login_user.html')

@login_required(login_url='/login/')
def logout_user(request):
    if request.method == 'POST':
        # User confirmed the logout, perform logout and redirect
        logout(request)
        return redirect('login-user')

    return render(request, 'authenticate/logout_user.html')

@login_required(login_url='/login/')
def homepage(request):
    return render(request, 'authenticate/homepage.html')
    



