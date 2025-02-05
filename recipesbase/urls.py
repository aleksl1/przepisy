from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:category_id>/", views.category, name="category"),
    path("recipe/<int:recipe_id>/", views.recipe, name="recipe"),
]