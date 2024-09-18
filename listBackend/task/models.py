from django.db import models


# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=50, blank=False)
    task_details = models.CharField(max_length=1000, blank=False)
    # picture = models.FileField(upload_to="foodapp_pics", blank=True, null=True)

    def __str__(self):
        return self.task_id
