from django.db import models

# Create your models here.
"""
Author
- name - charfield
- bio - textfield

Recipe
- title - charfield
- author - foreignkey
- description - textfield
- time required - charfield
- instructions - textfield
"""


class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.author.name}"
