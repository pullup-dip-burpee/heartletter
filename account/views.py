from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# not fully implemented
def main(request):
    return render(request, 'main.html')
    
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password"]
            )
            auth.login(request, user)
            return redirect('main')
        return render(request, 'signup.html')
        
    return render(request, 'signup.html')
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main')