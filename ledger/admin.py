from django.contrib import admin

from .models import Profile, Ingredient, Recipe, RecipeIngredient, RecipeImage




class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    search_fields = ['name']
    list_display = ['name']


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ['name']
    list_display = ['name', 'author']
    

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class RecipeWithInlineAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ['name', 'author']
    inlines = [RecipeIngredientInline, RecipeImageInline]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ['name']
    list_display = ['name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeWithInlineAdmin)