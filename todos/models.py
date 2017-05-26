from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class HashTag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    hashtags = models.ManyToManyField(HashTag)
