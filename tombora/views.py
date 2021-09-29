from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def homePage(request):

    context = {}
    return render(request, 'tombora/index.html', context)


def register(request):
    context = {}
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if request.POST.get('username') and request.POST.get('password1') and request.POST.get('email'):
                user = User.objects.create_user(
                    first_name=request.POST.get('firstname'),
                    last_name=request.POST.get('lastname'),
                    username=request.POST.get('username'),
                    email=request.POST.get('email'),
                    password=request.POST.get('password1'),
                )
                messages.success(request, 'User created successfully!!')
                return render(request, 'tombora/register.html', context)
            else:
                messages.success(request, 'something went wrong!!')
                return render(request, 'tombora/register.html', context)
        else:
            messages.success(request, 'password dont match')
            return render(request, 'tombora/register.html', context)
    else:
        return render(request, 'tombora/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')
        else:
            messages.info(request, 'Username Or password is incorrect')
    return render(request, 'tombora/login.html')


def logOutUser(request):

    logout(request)
    return redirect('login')

