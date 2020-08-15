from django.shortcuts import HttpResponseRedirect, render, reverse
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recipe_box_app.models import Author, Recipe
from recipe_box_app.forms import AddAuthorForm, AddRecipeForm, AddLoginForm, AddSignupForm


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


@login_required
def add_author(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(
                    username=data.get("username"),
                    password=data.get("password")
                )
                Author.objects.create(
                    name=data.get("name"),
                    bio=data.get("bio"),
                    user=new_user
                )
            return HttpResponseRedirect(reverse("homepage"))
    else:
        return HttpResponseForbidden(
            "Authors cannot be added by non-staff members."
        )
    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        # new_recipe = form.save(commit=False)
        # new_recipe.author = request.User.author
        # new_recipe.save()
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=request.user.author,
                description=data.get('description'),
                time_required=data.get('time_required'),
                instructions=data.get('instructions'),
            )
        return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, "generic_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AddLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data.get("username"),
                password=data.get("password")
            )
            if user:
                login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse("homepage"))
            )

    form = AddLoginForm()
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = AddSignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data.get("username"),
                password=data.get("password")
            )
            Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = AddSignupForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
