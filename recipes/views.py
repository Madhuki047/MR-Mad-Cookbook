from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe


def home(request):
    latest_recipes = Recipe.objects.filter(is_published=True)[:6]
    categories = Category.objects.all()
    context = {
        'latest_recipes': latest_recipes,
        'categories': categories,
    }
    return render(request, 'recipes/home.html', context)


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'recipes/category_list.html', {'categories': categories})


def recipe_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    recipes = category.recipes.filter(is_published=True)
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'current_category': category,
    })


def recipe_list(request):
    q = request.GET.get('q', '')
    recipes = Recipe.objects.filter(is_published=True)
    if q:
        recipes = recipes.filter(title__icontains=q)
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'search_query': q,
    })


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, is_published=True)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
