from django.contrib import admin
from .models import Task, TaskCategory, Creator

admin.site.register(Task)
admin.site.register(TaskCategory)

