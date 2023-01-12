from rest_framework import serializer, viewsets
from .models import TodoItem

class TodoSerializer(serializer.Serializer):
    class Meta:
        model = TodoItem
        fields = ['id' , 'todoId' , 'label', 'done']