from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('Recipe', blank=True, related_name='favorite_recipes')

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
