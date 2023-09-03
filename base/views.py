from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def homeview(request):
    return render(request, 'base/index.html')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('../account/')
        else:
            messages.error(request, 'Username or Password does not exist')

    return render(request, 'base/index.html')


@login_required(login_url='base:login')
def welcomeview(request):
    return render(request, 'base/account.html')


def registerview(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect('base:login')
        except:
            messages.error(request, 'an error occurred during registration')
    else:
        form = MyUserCreationForm()
    return render(request, 'base/register.html', {'form': form})


def logoutuser(request):
    logout(request)
    return redirect('base:login')
