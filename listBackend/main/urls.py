from django.urls import path
from .views import UserTaskListView, UserTaskByCategoryView

urlpatterns = [
    path('tasks/', UserTaskListView.as_view(), name='user-task-list'),
    path('tasks/category/<int:category_id>/', UserTaskByCategoryView.as_view(), name='user-task-by-category'),
]
