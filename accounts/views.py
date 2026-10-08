from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages  # Helps show errors on screen
from django.contrib.auth import authenticate

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        # Safety Check 1: Do the passwords match?
        if password1 != password2:
            print("Passwords do not match")
            messages.info(request, "Passwords do not match")
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        # Safety Check 2: Does the username already exist?
        if User.objects.filter(username=username).exists():
            print("Username taken")
            messages.info(request, "Username taken")
            return render(request, 'register.html', {'error': 'Username already taken'})
 
        # If everything passes, create the user
        user = User.objects.create_user(
            username=username, 
            password=password1, 
            email=email, 
            first_name=first_name, 
            last_name=last_name
        )
        user.save()
        messages.info(request,'User Created Successfully!')
        print('User Created Successfully!')
        
        # Absolute path redirect to guarantee it goes to the right place
        return render(request,'login.html')

    else:
        # Handles the GET request
        return render(request, 'register.html', {})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return render(request, 'login.html')
            
    # ✅ FIX: Added the else block to handle the GET request
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')