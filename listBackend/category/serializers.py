from rest_framework import serializers
from . import models




class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields=['title', 'category_id']