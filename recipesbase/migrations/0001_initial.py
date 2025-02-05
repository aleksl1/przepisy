# Generated by Django 5.1.5 on 2025-01-20 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('ingredients', models.TextField(help_text='List of ingredients and quantities')),
                ('instructions', models.TextField(help_text='Step-by-step cooking instructions')),
                ('calories', models.PositiveIntegerField(help_text='Total calories in kcal')),
                ('protein', models.FloatField(help_text='Protein content in grams')),
                ('fat', models.FloatField(help_text='Fat content in grams')),
                ('carbs', models.FloatField(help_text='Carbohydrate content in grams')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipesbase.category')),
            ],
        ),
    ]
