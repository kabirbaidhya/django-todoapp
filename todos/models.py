from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
