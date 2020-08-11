from django.shortcuts import render, HttpResponseRedirect, reverse

from recipe_box_app.models import Author, Recipe
from recipe_box_app.forms import AddAuthorForm, AddRecipeForm


# Create your views here.
def index_view(request):
    initial_index = Recipe.objects.all()
    return render(request, "index.html", {"index": initial_index,
                                          "homepage": "Recipe Box"})


def author_view(request, author_id):
    all_authors = Author.objects.filter(id=author_id).first()
    all_authors_recipes = Recipe.objects.filter(author=all_authors)
    return render(request, "authors.html", {"authors": all_authors,
                                            "recipes": all_authors_recipes,
                                            "post": all_authors})


def recipe_view(request, recipe_id):
    all_recipes = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipes.html", {"recipes": all_recipes,
                                            "post": all_recipes})


def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form})


# def author_post_detail(request, author_post_id):
#     new_author = Author.objects.filter(id=author_post_id).first()
#     return render(request, "authors.html", {"post": new_author})


def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                description=data.get('description'),
                time_required=data.get('time_required'),
                instructions=data.get('instructions'),
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, "generic_form.html", {"form": form})


# def recipe_post_detail(request, recipe_post_id):
#     new_recipe = Author.objects.filter(id=recipe_post_id).first()
#     return render(request, "recipes.html", {"post": new_recipe})
