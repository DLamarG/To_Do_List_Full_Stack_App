from django.db import models
from django.contrib.auth.models import User





# TaskCreator Models

class Creator(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

