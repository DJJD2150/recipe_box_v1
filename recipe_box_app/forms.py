from django import forms
from recipe_box_app.models import Author, Recipe


class AddAuthorForm(forms.ModelForm):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = Author
        fields = ["name", "bio"]


class AddRecipeForm(forms.ModelForm):
    class Meta():
        model = Recipe
        fields = ["title", "description", "time_required", "instructions"]
    # title = forms.CharField(max_length=50)
    # # author = forms.ModelChoiceField(queryset=Author.objects.all())
    # description = forms.CharField(widget=forms.Textarea)
    # time_required = forms.CharField(max_length=50)
    # instructions = forms.CharField(widget=forms.Textarea)


class AddLoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class AddSignupForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
