from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "ledger/recipe_list.html", ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {"recipe": recipe}
    return render(request, "ledger/recipe_detail.html", ctx)


