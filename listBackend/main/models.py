from django.db import models
from django.contrib.auth.models import User
from task.models import Task




#Author model.
class Author(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    my_recipes = models.ManyToManyField(Task, related_name='my_recipes', blank=True)


    def add_to_recipes(self, task_title, task_details, task_id):
        if not self.my_recipes.filter(task_title=task_title).exists():
            recipe=Task.objects.create(task_id=task_id, task_title=task_title, task_details=task_details)
            self.my_recipes.add(recipe)
            return {'message': 'recipe added to your recipes'}
        else:
            return {'message': 'recipe already exist'}
        

    def __str__(self):
        return self.user.username



# # Category
# class Category(models.Model):
#     title = models.CharField(max_length=15, choices=TITLE_CHOICES)
#     details=models.TextField(null=True, max_length=500)
#     category_id=models.CharField(primary_key=True)