from django.shortcuts import render
from django.http import HttpResponse
from todos.models import Todo


def index(request):
    items = Todo.objects.all()

    return render(request, 'index.html', {'items': items})


def create(request):
    return render(request, 'create.html')


def save(request):
    return HttpResponse('Save TODO item here.')
