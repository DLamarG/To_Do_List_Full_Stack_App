from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task, TaskCategory
from .serializers import TaskSerializer, TaskCategorySerializer
from rest_framework.response import Response
from rest_framework import status

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
    


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user to the currently authenticated user
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # Override create method to return a custom response on success
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
