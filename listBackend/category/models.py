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
    category_title = models.CharField(max_length=15, choices=TITLE_CHOICES)
    