from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confir = request.POST.get('password_confir')
        
        if password != password_confir:
            print("Passwords don't match, bitch...")
            return redirect('/users/register/')
        
        if len(password) < 6:
            print('Password is too small, like your dick, asshole.')
            return redirect('/users/register/')
        
        users = User.objects.filter(username=username)
        print(users.exists())
        
        if users.exists():
            print('This name has already been taken, choose another one.')
            return redirect('/users/register/')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        return redirect('/users/login/')
    