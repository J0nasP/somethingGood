from rest_framework import serializers
from .models import TodoItem

class TodoSerializer(serializers.Serializer):
    class Meta:
        model = TodoItem
        fields = ['id' , 'todoId' , 'label', 'done']