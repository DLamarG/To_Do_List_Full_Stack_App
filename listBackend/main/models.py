from django.db import models
from django.contrib.auth.models import User

# TaskCategory Model
class TaskCategory(models.Model):
    CATEGORY_CHOICES = [
        (1, 'Applications'),
        (2, 'Networking'),
        (3, 'Meetings'),
        (4, 'Certifications'),
        (5, 'Interviews'),
        (6, 'Projects'),
    ]
    id = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.get_id_display()

# Task Model
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title