from rest_framework import serializers
from .models import TodoTask

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoTask
        fields = ['taskId', 'label', 'done']