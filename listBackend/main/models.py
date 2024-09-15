from django.db import models
from django.contrib.auth.models import User


TITLE_CHOICES = {
    "Applications",
    "Networking",
    "Interviews",
    "Coding",
    "Projects",
    "Certifications",
}

#Author model.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(null=True)



# Category
class Category(models.Model):
    title = models.CharField(max_length=15, choices=TITLE_CHOICES)
    details=models.TextField(null=True, max_length=500)
    category_id=models.CharField(primary_key=True)