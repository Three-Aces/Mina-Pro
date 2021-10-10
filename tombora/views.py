from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Member


def homePage(request):
    context = {}
    return render(request, 'tombora/index.html', context)


def register(request):
    if request.method == 'POST':
        # collecting data from register form
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        user_email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # checking if passwords are the same
        if password1 != password2:
            messages.info(request, 'password must be the same!')
            return redirect('tombora:register')

        else:
            data = Member(
                first_name=firstname,
                last_name=lastname,
                username=username,
                user_email=user_email,
                password=password1,
                retype_password=password2)

            data.save()  # saving data into db
            messages.success(request, 'successfully signedup')
            return redirect('tombora:login')
    else:
        return render(request, 'tombora/register.html')


def loginPage(request):
    if request.method == 'POST':
        # getting  data  from logi  form
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authenticate  member
        member = Member.memberAuth_objects.get(username=username, password=password)

        if member:
            # messages.success(request, 'welcome message')
            return HttpResponse(f'welcome ' + member.username)
        else:
            return HttpResponse('does\'t exist')
    else:
        return render(request, 'tombora/login.html')

def logOutUser(request):
    logout(request)
    return redirect('login')
