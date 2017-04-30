from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'app_title': 'TodoApp'
    }
    return render(request, 'index.html', context)


def create(request):
    return HttpResponse('This should display the create form.')
