from django.db import models

# Create your models here.


TITLE_CHOICES = {
    "Applications",
    "Networking",
    "Interviews",
    "Coding",
    "Projects",
    "Certifications",
}






class Category(models.Model):
    title = models.CharField(max_length=15, choices=TITLE_CHOICES)
    details=models.TextField(null=True, max_length=500)
    category_id=models.CharField(primary_key=True)