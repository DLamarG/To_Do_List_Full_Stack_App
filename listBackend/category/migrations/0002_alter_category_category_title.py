# Generated by Django 5.1.1 on 2024-09-24 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_title',
            field=models.CharField(choices=[('A', 'Applications'), ('N', 'Networking'), ('I', 'Interviews'), ('C', 'Coding'), ('P', 'Projects'), ('D', 'Development')], max_length=1),
        ),
    ]
