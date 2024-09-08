from django.db import models
from django.contrib.auth.models import User

class Creator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class TaskCategory(models.Model):
    APPLICATIONS = 'Applications'
    NETWORKING = 'Networking'
    PROJECTS = 'Projects'
    MEETINGS = 'Meetings'
    CERTIFICATIONS = 'Certifications'

    CATEGORY_CHOICES = [
        (APPLICATIONS, 'Applications'),
        (NETWORKING, 'Networking'),
        (PROJECTS, 'Projects'),
        (MEETINGS, 'Meetings'),
        (CERTIFICATIONS, 'Certifications'),
    ]

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default=APPLICATIONS,
    )

    def __str__(self):
        return self.category

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)  # Add the Creator foreign key
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)

    def formatted_created_at(self):
        """Return the created_at date in DD/MM/YYYY format."""
        return self.created_at.strftime('%d/%m/%Y')

    def __str__(self):
        return self.title
