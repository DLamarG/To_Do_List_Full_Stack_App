from rest_framework import serializers
from .models import Task, TaskCategory

# Serializer for TaskCategory
class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = ['id', 'name']

# Serializer for Task
class TaskSerializer(serializers.ModelSerializer):
    category = TaskCategorySerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'category', 'user', 'created_at', 'due_date']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        category_id = validated_data.pop('category_id')
        category = TaskCategory.objects.get(id=category_id)
        task = Task.objects.create(user=user, category=category, **validated_data)
        return task

