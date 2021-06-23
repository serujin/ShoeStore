from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'sign_up.html', context={'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', context={'form': form})

def sign_in(request):
    if request.user.is_authenticated:
        login(request, request.user)
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'sign_in.html', context={'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html', context={'form': form})

def logout(request):
    auth_logout(request)
    return redirect('sign_in')
