from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            ...
        else:
            messages.success(request, ("Incorrect username or password."))
            return redirect('sign_in')
    else:
        return render(request, 'registration/sign_in.html', {})