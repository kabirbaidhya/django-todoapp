from django.contrib import admin

# Register your models here.
from .models import Todo, HashTag

admin.site.register(Todo)
admin.site.register(HashTag)
