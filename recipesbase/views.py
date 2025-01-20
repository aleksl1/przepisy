from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe, Category


# Create your views here.

def index(request):
    
    # Fetch all recipes
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        recipes = recipes.filter(category_id=category_id)

    return render(request, "recipesbase/index.html", {"recipes": recipes, "categories": categories})


# def index(request):
#     categories = Category.objects.all()
#     recipes = Recipe.objects.all()

#     # Get category filter from the URL query parameters
#     # category_id = request.GET.get('category')
#     # if category_id:
#     #     recipes = recipes.filter(category_id=category_id)

#     # context = {
#     #     'categories': categories,
#     #     'recipes': recipes,
#     # }
#     return render(request, 'recipesbase/index.html', recipes)

def category(request, category_id):
    return HttpResponse("This is the category view. %s", category_id) 

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "recipesbase/recipe.html", {"recipe": recipe})