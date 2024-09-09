from django.urls import path
from .views import UserTaskListView, TaskCategoryView, TaskCreateView

urlpatterns = [
    path('tasks/', UserTaskListView.as_view(), name='user-tasks'),  # List tasks for logged-in user
    path('tasks/category/<str:category>/', TaskCategoryView.as_view(), name='tasks-by-category'),  # List tasks by category
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),  # Create a new task
]