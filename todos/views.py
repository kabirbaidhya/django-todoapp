from django.shortcuts import render


def index(request):
    context = {
        'app_title': 'TodoApp'
    }
    return render(request, 'index.html', context)
