from django.contrib import admin
from .models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'created_at', 'is_published')
    list_filter = ('difficulty', 'category', 'is_published')
    search_fields = ('title', 'ingredients')
    prepopulated_fields = {'slug': ('title',)}