from django.contrib import messages
from django.shortcuts import render, redirect

def login(request):
    print('The login page')

    return render(request, 'login.html')
