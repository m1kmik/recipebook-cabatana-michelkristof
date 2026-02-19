from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name']
    

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    fk_name = 'recipe'

class RecipeWithInlineAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [RecipeIngredientInline]


admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeWithInlineAdmin) 