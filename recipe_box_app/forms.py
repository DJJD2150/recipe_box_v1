from django import forms
from recipe_box_app.models import Author, Recipe


class AddAuthorForm(forms.Form):
    # username = forms.CharField(max_length=240)
    name = forms.CharField(max_length=80)
    bio = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)


class AddLoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class AddSignupForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
