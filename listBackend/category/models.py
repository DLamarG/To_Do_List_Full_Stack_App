from django.db import models

# Create your models here.


TITLE_CHOICES = {
    "A": "Applications",
    "N": "Networking",
    "I": "Interviews",
    "C": "Coding",
    "P": "Projects",
    "D": "Development",
}

# SHIRT_SIZES = {
#         "S": "Small",
#         "M": "Medium",
#         "L": "Large",
#     }


class Category(models.Model):
    category_title = models.CharField(max_length=1, choices=TITLE_CHOICES)
    