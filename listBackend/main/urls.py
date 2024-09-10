from django.urls import path
from .views import UserTaskListView, UserTaskByCategoryView, TaskCreateView

urlpatterns = [
    path('tasks/', UserTaskListView.as_view(), name='user-task-list'),
    path('tasks/category/<int:category_id>/', UserTaskByCategoryView.as_view(), name='user-task-by-category'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
]
