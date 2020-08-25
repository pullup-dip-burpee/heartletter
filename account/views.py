from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

#sign in
def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'sign_in.html', {'error':'username or password is incorrect'})
    return render(request, 'sign_in.html')

def sign_up(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password"]
            )
            auth.login(request, user)
            return redirect('main')
        return render(request, 'sign_up.html')
        
    return render(request, 'sign_up.html')