from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confir = request.POST.get('password_confir')
        
        if password != password_confir:
            messages.add_message(request, constants.ERROR, 'As senhas digitadas não são iguais, tente novamente.')
            return redirect('/users/register/')
        
        if len(password) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres')
            return redirect('/users/register/')
        
        users = User.objects.filter(username=username)
        print(users.exists())
        
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Alguém já pegou este nome de usuário, tente algum outro.')
            return redirect('/users/register/')
        
        users = User.objects.filter(email=email)
        print(users.exists())
        
        if users.exists():
            messages.add_message(request, constants.ERROR, 'O e-mail que vocês está tentando registrar já pertence a alguém, tente algum outro.')
            return redirect('/users/register/')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        return redirect('/users/register/')
    
    
def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user:
            auth.login(request, user)
            return redirect('/pacients/home')
        
        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
        return redirect('/users/login/')