from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes")
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(help_text="List of ingredients and quantities")
    instructions = models.TextField(help_text="Step-by-step cooking instructions")
    calories = models.PositiveIntegerField(help_text="Total calories in kcal")
    protein = models.FloatField(help_text="Protein content in grams")
    fat = models.FloatField(help_text="Fat content in grams")
    carbs = models.FloatField(help_text="Carbohydrate content in grams")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name