from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    items = [
        {
            'title': 'Item 1',
            'completed': False,
            'description': 'No eam nisl assum impetus, dicta .',
            'created_at': 'Apr 30, 2017'
        },
        {
            'title': 'Item 2',
            'completed': True,
            'description': 'No eam nisl assum impetus, dicta .',
            'created_at': 'Apr 30, 2017'
        },
        {
            'title': 'Item 3',
            'completed': False,
            'description': 'No eam nisl assum impetus, dicta .',
            'created_at': 'Apr 30, 2017'
        }
    ]

    return render(request, 'index.html', {
        'items': items
    })


def create(request):
    return render(request, 'create.html')
