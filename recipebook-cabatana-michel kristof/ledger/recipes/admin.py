from django.contrib import admin

from .models import Profile, Ingredient, Recipe, RecipeIngredient




class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    search_fields = ['name']
    list_display = ['name']


class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    fk_name = 'recipe'


class RecipeWithInlineAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [RecipeIngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ['name']
    list_display = ['name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeWithInlineAdmin)
 

