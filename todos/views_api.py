import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from todos.models import Todo


@csrf_exempt
@require_http_methods(['PATCH'])
def update(request, id):
    # Get the params from the payload.
    data = json.loads(request.body.decode('utf-8'))

    print('Received update API request for todo id: ', id)
    print('Completed: ', data['completed'])

    return JsonResponse({})
