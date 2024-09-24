# Generated by Django 5.1.1 on 2024-09-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(choices=[('A', 'Applications'), ('N', 'Networking'), ('I', 'Interviews'), ('C', 'Coding'), ('P', 'Projects'), ('D', 'Development')], max_length=1)),
            ],
        ),
    ]
