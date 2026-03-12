from django.contrib import admin

from .models import Profile, Ingredient, Recipe, RecipeIngredient




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


class RecipeWithInlineAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']
    inlines = [RecipeIngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ['name']
    list_display = ['name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeWithInlineAdmin)