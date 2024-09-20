from rest_framework import serializers
from . import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields=['user', 'my_task']