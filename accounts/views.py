from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                    username = request.POST["username"],
                    password = request.POST["password"],
            )
            auth.login(request, user)
            return redirect('main')
        return render(request, 'sign_up.html')
