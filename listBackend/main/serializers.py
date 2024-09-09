from rest_framework import serializers
from .models import Task, TaskCategory

class TaskSerializer(serializers.ModelSerializer):
    formatted_created_at = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ['title', 'description', 'created_at', 'formatted_created_at', 'creator', 'category']

    
    def create(self, validated_data):
        """ Override the create method to associate the task with the logged-in user. """
        user = self.context['request'].user
        creator = user.creator  # Assuming the user has an associated Creator object
        task = Task.objects.create(creator=creator, **validated_data)
        return task
