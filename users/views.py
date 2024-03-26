from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
            ...
        else:
            messages.success(request, ("Incorrect username or password."))
            return redirect('sign_in')
    else:
        return render(request, 'authenticate/sign_in.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('start')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Patienten')  # Gruppe "Patient" abrufen
            user.groups.add(group)  # Benutzer zur "Patient"-Gruppe hinzufügen
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration succeeded"))
            return redirect('dashboard')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/sign_up.html', {'form':form,})