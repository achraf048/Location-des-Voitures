from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm , UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            return redirect('accueil')
            
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user() 
            login(request, user) 
            return redirect('accueil') 
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})
