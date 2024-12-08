from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import User  # Replace with your actual app name

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if username == "Robinson Amianda" or email == "robinsonamianda5@gmail.com" or password == "1234":
            return redirect("home")




def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

