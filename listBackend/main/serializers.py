from rest_framework import serializers
from .models import Task, TaskCategory

class TaskSerializer(serializers.ModelSerializer):
    formatted_created_at = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ['title', 'description', 'created_at', 'formatted_created_at', 'creator', 'category']
