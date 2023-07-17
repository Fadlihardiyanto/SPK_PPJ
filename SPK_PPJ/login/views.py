from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            request.session['NimOrNip'] = user.NimOrNip
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid nim/nip or password, or your account is not active.')
    else:
        form = LoginForm()
    
    return render(request, 'login/login_view.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login/')

