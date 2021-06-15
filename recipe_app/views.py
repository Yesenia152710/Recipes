from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from recipe_app.models import Recipe, Author
from recipe_app.forms import AddRecipeForm, AddAuthorForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    published = Recipe.objects.all()
    return render(request, 'index.html', {'published': published})


def recipe_detail(request, pub_id: int):
    publish = Recipe.objects.get(id=pub_id)
    return render(request, 'recipe_detail.html', {'publish': publish})


def author_detail(request, auth_id: int):
    my_au = Author.objects.get(id=auth_id)
    author_pub = Recipe.objects.filter(author=my_au)
    return render(request, 'auther_detail.html',
                  {'author': my_au, 'publisher': author_pub})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    log = logout(request)
    return redirect('homepage')


@login_required
def add_author(request):
    if not request.user.is_staff:
        return HttpResponse('ERROR: You do not have permission to add an author')
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'], password=data['password'])
            Author.objects.create(au_name=data['au_name'], user=user)
            return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()
    return render(request, 'generic_form.html', {'form': form})


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_publish = Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                ingredience=data['ingredience'],
                body=data['body']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddRecipeForm()
    return render(request, 'generic_form.html', {'form': form})
