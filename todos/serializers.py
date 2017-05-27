from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    ''' Serializer to map the Todo model to JSON. '''

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Todo
        fields = ('id', 'title', 'description', 'completed', 'created_at', 'user')
        read_only_fields = ('created_at', 'id')
