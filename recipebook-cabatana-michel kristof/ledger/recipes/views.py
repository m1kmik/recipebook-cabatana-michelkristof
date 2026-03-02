from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "recipes/recipe_list.html", ctx)


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
