from django.shortcuts import render

from recipe_box_app.models import Author, Recipe


# Create your views here.
def index_view(request):
    initial_index = Recipe.objects.all()
    return render(request, "index.html", {"index": initial_index,
                                          "homepage": "Recipe Box"})


def author_view(request, author_id):
    all_authors = Author.objects.filter(id=author_id).first()
    all_authors_recipes = Recipe.objects.filter(author=all_authors)
    return render(request, "authors.html", {"authors": all_authors,
                                            "recipes": all_authors_recipes})


def recipe_view(request, recipe_id):
    all_recipes = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipes.html", {"recipes": all_recipes})
