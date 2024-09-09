from rest_framework import generics
from .models import Task, TaskCategory
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
# from rest_framework.permissions import IsAuthenticated

class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(creator__user=self.request.user)


class TaskCategoryView(generics.ListAPIView):
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category = self.kwargs['category']  # Capture the category from the URL
        # Get the TaskCategory object for the given category
        task_category = get_object_or_404(TaskCategory, category=category)
        # Filter tasks by the given category and the logged-in user
        return Task.objects.filter(category=task_category, creator__user=self.request.user)



class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to create tasks

    def perform_create(self, serializer):
        """ Automatically set the creator to the logged-in user. """
        serializer.save(creator=self.request.user.creator)