from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth import login, logout, user_logged_in, user_logged_out, authenticate
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return render(request, 'orders/index.html', context={'type': 'success', 'message': 'Successfully Logged Out', 'username': request.user.username})


def index(request):
    return render(request, 'orders/index.html', context={'username': request.user.username})


def register(request):
    if request.POST.get('username') == None:
        return render(request, 'orders/register.html')

    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.create_user(username, email, password)
        if password != confirm_password:
            return render(request, 'orders/register.html', context={'type': 'danger', 'message': 'Please match the passwords first!', 'username': request.user.username})
    except:
        return render(request, 'orders/register.html', context={'type': 'danger', 'message': 'This username is already taken', 'username': request.user.username})
    user.last_name = last_name
    user.first_name = first_name
    user.save()
    i = authenticate(request, username=username, password=password)
    login(request, i)
    return render(request, 'orders/index.html', context={'type': 'success', 'message': 'Successfully Logged In', 'username': request.user.username})


def login_view(request):
    if request.POST.get('username') == None:
        return render(request, 'orders/login.html')
    username = request.POST['username']
    password = request.POST['password']
    i = authenticate(request, username=username, password=password)
    if i:
        login(request, i)
        return render(request, 'orders/index.html', context={'type': 'success', 'message': 'Successfully Logged In', 'username': request.user.username})
    else:
        return render(request, 'orders/login.html', context={'type': 'success', 'message': 'Invalid Credentials, please try again', 'username': request.user.username})

