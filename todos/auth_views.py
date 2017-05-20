from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect

def login(request):
    print('The login page')

    return render(request, 'login.html')

def logout(request):
    print('Logging Out')
    auth.logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('index')

def authenticate(request):
    print('The authenticate request')
    # Get the form data from the request.
    username = request.POST.get('username')
    password = request.POST.get('password')

    print('Authenticating the user')
    user = auth.authenticate(request, username=username, password=password)

    # If authentication failed redirect back to the form
    # with messages.
    if not user:
        print('Login error')
        messages.error(request, 'Login failed. Please try again.')
        return redirect(request.META.get('HTTP_REFERER'))

    # If authentication was successful
    auth.login(request, user)
    print('Login successful')

    # Add save success message
    messages.info(request, 'You are now logged in as {}.'.format(username))
    return redirect('index')
