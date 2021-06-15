from django import forms
from recipe_app.models import Author


# class AddAuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ['au_name']

class AddAuthorForm(forms.Form):
    au_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=40)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    ingredience = forms.CharField(widget=forms.Textarea)
    body = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
