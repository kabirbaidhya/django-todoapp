from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login(request):
    print('The login page')

    return render(request, 'login.html')

def authenticate(request):
    print('The authenticate request')
    # Get the form data from the request.
    username = request.POST.get('username')
    password = request.POST.get('password')

    print('Authenticating the user')
    user = authenticate(username=username, password=password)

    # If authentication failed redirect back to the form
    # with messages.
    if not user:
        print('Login error')
        messages.error(request, 'Login failed. Please try again.')
        return redirect(request.META.get('HTTP_REFERER'))

    # If authentication was successful
    login(request, user)
    print('Login successful')

    # Add save success message
    messages.info(request, 'You are now logged in as {}.'.format(username))
    redirect('index')
