# Generated by Django 5.1.1 on 2024-09-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcategory',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
