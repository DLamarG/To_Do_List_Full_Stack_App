from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task, TaskCategory
from .serializers import TaskSerializer, TaskCategorySerializer

# View for listing tasks for the logged-in user
class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# View for listing tasks by category for a user
class UserTaskByCategoryView(generics.ListAPIView):
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Task.objects.filter(user=self.request.user, category_id=category_id)
