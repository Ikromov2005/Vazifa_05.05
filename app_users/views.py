from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm , UserLoginForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hisobingiz yaratildi! {username}, tizimga kirish uchun tayyor!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'app_users/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
    else:
        form = UserLoginForm()
    return render(request, 'app_users/login.html', {'form': form})
